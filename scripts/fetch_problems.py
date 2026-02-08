#!/usr/bin/env python3
"""
fetch_problems.py
=================
Fetches LeetCode problems (up to ID 2500) using:
  1. REST API  -> problem list with metadata (free + premium)
  2. GraphQL   -> individual problem descriptions, examples, tags, code snippets
  3. Optional auth.json -> session cookies for premium content

Outputs: scripts/problems.json  (cached, incremental -- safe to re-run)

Usage:
    python3 scripts/fetch_problems.py [--max-id 2500] [--workers 4]
"""

import json
import os
import sys
import time
import html
import re
import argparse
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

sys.stdout.reconfigure(line_buffering=True)

SCRIPT_DIR = Path(__file__).resolve().parent
CACHE_FILE = SCRIPT_DIR / "problems.json"
AUTH_FILE = SCRIPT_DIR / "auth.json"

LEETCODE_API = "https://leetcode.com/api/problems/algorithms/"
LEETCODE_GRAPHQL = "https://leetcode.com/graphql"

BASE_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Referer": "https://leetcode.com",
}

GRAPHQL_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    difficulty
    content
    isPaidOnly
    topicTags {
      name
      slug
    }
    exampleTestcases
    codeSnippets {
      lang
      langSlug
      code
    }
    hints
    sampleTestCase
  }
}
"""

# Thread-safe counter
_lock = threading.Lock()
_counter = {"fetched": 0, "cached": 0, "failed": 0}


def load_auth_cookies():
    """Load session cookies from auth.json if present."""
    if AUTH_FILE.exists():
        with open(AUTH_FILE) as f:
            data = json.load(f)
        cookies = data.get("cookies", {})
        if "LEETCODE_SESSION" in cookies:
            print(f"  Auth loaded: LEETCODE_SESSION present (premium access enabled)")
            return cookies
    print("  No auth.json with LEETCODE_SESSION found (premium content will be limited)")
    return {}


def make_headers(cookies=None):
    """Build headers, optionally with auth cookies."""
    headers = dict(BASE_HEADERS)
    if cookies:
        cookie_str = "; ".join(f"{k}={v}" for k, v in cookies.items())
        headers["Cookie"] = cookie_str
        if "csrftoken" in cookies:
            headers["X-CSRFToken"] = cookies["csrftoken"]
    return headers


def fetch_json(url, data=None, headers=None):
    """Fetch JSON from a URL. If data is provided, POST it."""
    headers = headers or BASE_HEADERS
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        req = Request(url, data=body, headers=headers, method="POST")
    else:
        req = Request(url, headers=headers)

    for attempt in range(3):
        try:
            with urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError) as e:
            if attempt < 2:
                time.sleep(2 ** (attempt + 1))
            else:
                return None
    return None


def strip_html(html_str):
    """Convert HTML problem description to plain text."""
    if not html_str:
        return ""
    text = re.sub(r"<[^>]+>", "", html_str)
    text = html.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def fetch_problem_list(max_id):
    """Fetch the full problem list from the REST API."""
    print("Fetching problem list from REST API...")
    data = fetch_json(LEETCODE_API)
    if not data or "stat_status_pairs" not in data:
        print("ERROR: Could not fetch problem list.")
        sys.exit(1)

    problems = []
    for item in data["stat_status_pairs"]:
        stat = item["stat"]
        fid = stat.get("frontend_question_id", stat.get("question_id", 0))
        if fid is None or fid > max_id:
            continue

        problems.append({
            "id": fid,
            "title": stat.get("question__title", ""),
            "slug": stat.get("question__title_slug", ""),
            "difficulty_level": item.get("difficulty", {}).get("level", 0),
            "paid_only": item.get("paid_only", False),
            "total_accepted": stat.get("total_acs", 0),
            "total_submitted": stat.get("total_submitted", 0),
        })

    problems.sort(key=lambda p: p["id"])
    free = sum(1 for p in problems if not p["paid_only"])
    premium = sum(1 for p in problems if p["paid_only"])
    print(f"  Found {len(problems)} problems with ID <= {max_id} (free: {free}, premium: {premium})")
    return problems


def fetch_single_problem(prob, headers, total):
    """Fetch a single problem's detail via GraphQL. Thread-safe."""
    slug = prob["slug"]
    payload = {
        "operationName": "questionData",
        "variables": {"titleSlug": slug},
        "query": GRAPHQL_QUERY,
    }
    data = fetch_json(LEETCODE_GRAPHQL, data=payload, headers=headers)

    if data and "data" in data and data["data"].get("question"):
        detail = data["data"]["question"]
        difficulty_map = {1: "Easy", 2: "Medium", 3: "Hard"}
        entry = {
            "id": prob["id"],
            "title": detail.get("title", prob["title"]),
            "slug": prob["slug"],
            "difficulty": detail.get("difficulty", difficulty_map.get(prob["difficulty_level"], "Unknown")),
            "content": detail.get("content", ""),
            "content_text": strip_html(detail.get("content", "")),
            "topic_tags": [t["name"] for t in (detail.get("topicTags") or [])],
            "topic_slugs": [t["slug"] for t in (detail.get("topicTags") or [])],
            "example_testcases": detail.get("exampleTestcases", ""),
            "sample_test_case": detail.get("sampleTestCase", ""),
            "hints": detail.get("hints", []),
            "python3_snippet": "",
            "paid_only": detail.get("isPaidOnly", prob.get("paid_only", False)),
            "total_accepted": prob["total_accepted"],
            "total_submitted": prob["total_submitted"],
        }
        for snippet in (detail.get("codeSnippets") or []):
            if snippet.get("langSlug") == "python3":
                entry["python3_snippet"] = snippet.get("code", "")
                break
        with _lock:
            _counter["fetched"] += 1
            done = _counter["fetched"] + _counter["cached"]
            if done % 50 == 0:
                print(f"    Progress: {done}/{total} ({_counter['fetched']} fetched, {_counter['cached']} cached)")
        return entry
    else:
        # Stub for premium or failed
        with _lock:
            _counter["failed"] += 1
        return {
            "id": prob["id"],
            "title": prob["title"],
            "slug": prob["slug"],
            "difficulty": {1: "Easy", 2: "Medium", 3: "Hard"}.get(prob["difficulty_level"], "Unknown"),
            "content": "",
            "content_text": "",
            "topic_tags": [],
            "topic_slugs": [],
            "example_testcases": "",
            "sample_test_case": "",
            "hints": [],
            "python3_snippet": "",
            "paid_only": prob.get("paid_only", True),
            "total_accepted": prob["total_accepted"],
            "total_submitted": prob["total_submitted"],
        }


def load_cache():
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-id", type=int, default=2500, help="Max problem ID to fetch")
    parser.add_argument("--workers", type=int, default=4, help="Concurrent fetch workers")
    args = parser.parse_args()

    print(f"=== LeetCode Problem Fetcher (ID 1-{args.max_id}) ===")

    # Load auth
    cookies = load_auth_cookies()
    headers = make_headers(cookies)

    # Load existing cache
    cache = load_cache()
    existing = {str(p["id"]): p for p in cache.get("problems", [])}
    print(f"  Existing cache: {len(existing)} problems")

    # Get problem list
    problem_list = fetch_problem_list(args.max_id)
    total = len(problem_list)

    # Split into cached vs to-fetch
    to_fetch = []
    results = []
    for prob in problem_list:
        pid = str(prob["id"])
        if pid in existing and existing[pid].get("content"):
            results.append(existing[pid])
            with _lock:
                _counter["cached"] += 1
        elif pid in existing and existing[pid].get("paid_only") and not cookies.get("LEETCODE_SESSION"):
            # Premium without auth -- keep existing stub
            results.append(existing[pid])
            with _lock:
                _counter["cached"] += 1
        else:
            to_fetch.append(prob)

    print(f"  Cached: {_counter['cached']}, To fetch: {len(to_fetch)}")

    if not to_fetch:
        print("Nothing new to fetch!")
        results.sort(key=lambda p: p["id"])
        save_cache({"problems": results, "count": len(results)})
        print(f"Done! {len(results)} problems in cache.")
        return

    # Fetch with thread pool (rate-limited)
    print(f"  Fetching {len(to_fetch)} problems with {args.workers} workers...")
    batch_size = 50

    for batch_start in range(0, len(to_fetch), batch_size):
        batch = to_fetch[batch_start:batch_start + batch_size]
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {}
            for i, prob in enumerate(batch):
                # Stagger requests
                time.sleep(0.3)
                f = executor.submit(fetch_single_problem, prob, headers, total)
                futures[f] = prob

            for f in as_completed(futures):
                result = f.result()
                if result:
                    results.append(result)

        # Checkpoint save
        results_sorted = sorted(results, key=lambda p: p["id"])
        save_cache({"problems": results_sorted, "count": len(results_sorted)})
        done = _counter["fetched"] + _counter["cached"]
        print(f"  [checkpoint] {done}/{total} saved ({_counter['failed']} failed)")

    # Final save
    results.sort(key=lambda p: p["id"])
    save_cache({"problems": results, "count": len(results)})

    with_content = sum(1 for p in results if p.get("content"))
    premium_no_content = sum(1 for p in results if p.get("paid_only") and not p.get("content"))
    print(f"\nDone! {len(results)} problems saved to {CACHE_FILE}")
    print(f"  With content: {with_content}")
    print(f"  Premium (no content): {premium_no_content}")
    print(f"  Failed: {_counter['failed']}")


if __name__ == "__main__":
    main()
