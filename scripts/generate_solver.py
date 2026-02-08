#!/usr/bin/env python3
"""
generate_solver.py
==================
Reads problems.json (from fetch_problems.py) and generates:
  - 18 chapter markdown files in P1/solver/
  - solution.py files in P1/solutions/problem_NNNN_slug/
  - solution.cpp files in P1/solutions/problem_NNNN_slug/
  - solution.md files in P1/solutions/problem_NNNN_slug/
  - Master solver.md index in P1/

Usage:
    python3 scripts/generate_solver.py [--chapters 1-6] [--force]
"""

import json
import os
import re
import sys
import html
import argparse
from pathlib import Path
from textwrap import dedent

sys.stdout.reconfigure(line_buffering=True)

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
CACHE_FILE = SCRIPT_DIR / "problems.json"
SOLVER_DIR = PROJECT_DIR / "solver"
SOLUTIONS_DIR = PROJECT_DIR / "solutions"

# ─────────────────────────────────────────────
# CHAPTER DEFINITIONS
# ─────────────────────────────────────────────
CHAPTERS = [
    ("01_arrays_and_hashing",       "Arrays and Hashing",           ["Array", "Hash Table", "Matrix", "Prefix Sum"]),
    ("02_two_pointers",             "Two Pointers",                 ["Two Pointers"]),
    ("03_sliding_window",           "Sliding Window",               ["Sliding Window"]),
    ("04_linked_list",              "Linked List",                  ["Linked List", "Doubly-Linked List"]),
    ("05_stack_and_queue",          "Stack and Queue",              ["Stack", "Queue", "Monotonic Stack", "Monotonic Queue"]),
    ("06_binary_search",            "Binary Search",                ["Binary Search"]),
    ("07_trees_and_bst",            "Trees and BST",                ["Tree", "Binary Tree", "Binary Search Tree"]),
    ("08_tries",                    "Tries",                        ["Trie"]),
    ("09_heap_and_priority_queue",  "Heap and Priority Queue",      ["Heap (Priority Queue)"]),
    ("10_backtracking",             "Backtracking",                 ["Backtracking"]),
    ("11_graphs",                   "Graphs",                       ["Graph", "Graph Theory", "Depth-First Search", "Breadth-First Search", "Topological Sort", "Union Find", "Union-Find", "Shortest Path"]),
    ("12_dynamic_programming",      "Dynamic Programming",          ["Dynamic Programming", "Memoization"]),
    ("13_greedy",                   "Greedy",                       ["Greedy"]),
    ("14_intervals",                "Intervals",                    ["Interval", "Line Sweep", "Sweep Line"]),
    ("15_math_and_bit_manipulation","Math and Bit Manipulation",    ["Math", "Bit Manipulation", "Number Theory", "Geometry", "Combinatorics", "Counting"]),
    ("16_string",                   "String",                       ["String", "String Matching"]),
    ("17_sorting_and_searching",    "Sorting and Searching",        ["Sorting", "Counting Sort", "Radix Sort", "Bucket Sort", "Merge Sort", "Quickselect"]),
    ("18_design",                   "Design",                       ["Design", "Data Stream", "Iterator", "Simulation", "Randomized"]),
]

# Priority order for classification (most specific first)
CHAPTER_PRIORITY = {tag: idx for idx, (_, _, tags) in enumerate(CHAPTERS) for tag in tags}


def classify_problem(topic_tags):
    """Classify a problem into a chapter based on its topic tags."""
    if not topic_tags:
        return "01_arrays_and_hashing"  # default

    # Score each chapter
    best_chapter = None
    best_priority = len(CHAPTERS) + 1

    # Specific overrides: these tags always win classification
    specific_tags = ["Trie", "Topological Sort", "Union Find", "Union-Find", "Sliding Window",
                     "Backtracking", "Design", "Data Stream", "Heap (Priority Queue)",
                     "Greedy", "Graph Theory", "Sorting", "Merge Sort", "Quickselect",
                     "Binary Search", "Linked List", "Doubly-Linked List",
                     "Line Sweep", "Sweep Line"]
    for tag in topic_tags:
        if tag in specific_tags:
            for ch_file, ch_name, ch_tags in CHAPTERS:
                if tag in ch_tags:
                    return ch_file

    # Otherwise use priority
    for tag in topic_tags:
        if tag in CHAPTER_PRIORITY:
            p = CHAPTER_PRIORITY[tag]
            if p < best_priority:
                best_priority = p
                best_chapter = CHAPTERS[p][0]

    return best_chapter or "01_arrays_and_hashing"


# ─────────────────────────────────────────────
# SOLUTION KNOWLEDGE BASE
# ─────────────────────────────────────────────
# Maps problem ID -> { "code": str, "pattern": str, "time": str, "space": str,
#                       "approach": str, "pseudocode": str }
# This is the core: optimal solutions for every problem.

from solutions_kb import SOLUTIONS_KB  # noqa: E402 -- imported after path setup
try:
    from solutions_kb_ext import SOLUTIONS_KB_EXT
    SOLUTIONS_KB.update(SOLUTIONS_KB_EXT)
except ImportError:
    pass
try:
    from solutions_kb_ext2 import SOLUTIONS_KB_EXT2
    SOLUTIONS_KB.update(SOLUTIONS_KB_EXT2)
except ImportError:
    pass
try:
    from solutions_kb_ext3 import SOLUTIONS_KB_EXT3
    # For ext3, merge animation_frames into existing entries without overwriting code
    for pid, data in SOLUTIONS_KB_EXT3.items():
        if pid in SOLUTIONS_KB:
            # Only add missing keys (like animation_frames)
            for key, val in data.items():
                if val and not SOLUTIONS_KB[pid].get(key):
                    SOLUTIONS_KB[pid][key] = val
        else:
            SOLUTIONS_KB[pid] = data
except ImportError:
    pass
print(f"  Solutions KB: {len(SOLUTIONS_KB)} hand-crafted solutions loaded")

# Auto-content engine for problems not in KB
from auto_content import (  # noqa: E402
    auto_generate_mermaid, auto_generate_approach, auto_generate_pseudocode,
    auto_complexity_time, auto_complexity_space, auto_generate_animation,
    auto_pattern_name, auto_generate_all, classify_pattern
)
print(f"  Auto-content engine loaded (pattern-based mermaid/pseudocode/animation)")

# Signature parser and solution templates
from sig_parser import parse_snippet, py_type_to_cpp, cpp_default  # noqa: E402
from solution_templates import (  # noqa: E402
    generate_solution_py, generate_solution_cpp,
    get_template, fill_template
)
print(f"  Solution template engine loaded (Python3 + C++ generation)")


def strip_html_to_md(html_str):
    """Convert HTML content to markdown-ish plain text."""
    if not html_str:
        return ""
    text = html_str
    # Convert common HTML to markdown
    text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text)
    text = re.sub(r"<b>(.*?)</b>", r"**\1**", text)
    text = re.sub(r"<em>(.*?)</em>", r"*\1*", text)
    text = re.sub(r"<i>(.*?)</i>", r"*\1*", text)
    text = re.sub(r"<code>(.*?)</code>", r"`\1`", text)
    text = re.sub(r"<pre>(.*?)</pre>", lambda m: "\n```\n" + re.sub(r"<[^>]+>", "", m.group(1)) + "\n```\n", text, flags=re.DOTALL)
    text = re.sub(r"<li>(.*?)</li>", r"- \1", text, flags=re.DOTALL)
    text = re.sub(r"</?ul>", "", text)
    text = re.sub(r"</?ol>", "", text)
    text = re.sub(r"<p>(.*?)</p>", r"\1\n", text, flags=re.DOTALL)
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"<sup>(.*?)</sup>", r"^\1", text)
    text = re.sub(r"</?div[^>]*>", "", text)
    text = re.sub(r"<img[^>]*>", "", text)
    text = re.sub(r"</?span[^>]*>", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def sanitize_dirname(slug):
    """Create a safe directory name from a problem slug."""
    return re.sub(r"[^a-z0-9_]", "_", slug.replace("-", "_"))


# ─────────────────────────────────────────────
# CHAPTER MARKDOWN GENERATOR
# ─────────────────────────────────────────────

def _get_solutions(prob):
    """Get Python and C++ solutions for a problem (KB or template-generated)."""
    pid = prob["id"]
    tags = prob.get("topic_tags", [])
    snippet = prob.get("python3_snippet", "")
    sol = SOLUTIONS_KB.get(pid, {})
    pattern = classify_pattern(tags)

    # Parse signature
    methods, is_design, cls_name = parse_snippet(snippet)

    # Python solution
    kb_code = sol.get("code")
    py_code = generate_solution_py(pattern, methods, cls_name, is_design, kb_solution=kb_code)

    # C++ solution
    cpp_code = generate_solution_cpp(pattern, methods, cls_name, is_design)

    return py_code, cpp_code, pattern, methods, is_design, cls_name


def generate_problem_section(prob):
    """Generate a full markdown section for one problem."""
    pid = prob["id"]
    title = prob["title"]
    slug = prob["slug"]
    difficulty = prob.get("difficulty", "Unknown")
    tags = prob.get("topic_tags", [])
    content_html = prob.get("content", "")

    sol = SOLUTIONS_KB.get(pid, {})
    # Auto-generate content for fields not in KB
    auto = auto_generate_all(tags, title)
    pattern = sol.get("pattern") or auto["pattern"]
    time_c = sol.get("time") or auto["time"]
    space_c = sol.get("space") or auto["space"]
    approach = sol.get("approach") or auto["approach"]
    pseudocode = sol.get("pseudocode") or auto["pseudocode"]
    mermaid = sol.get("mermaid") or auto["mermaid"]
    walkthrough = sol.get("walkthrough", "")
    animation = sol.get("animation_frames") or auto["animation_frames"]

    # Get solutions (Python + C++)
    py_code, cpp_code, _, _, _, _ = _get_solutions(prob)

    # Problem description
    is_premium = prob.get("paid_only", False) and not content_html
    description = strip_html_to_md(content_html)
    if not description:
        description = prob.get("content_text", "")
    if not description and is_premium:
        description = "*(Premium problem -- description requires LeetCode subscription)*"
    elif not description:
        description = "*(Description not available)*"

    lines = []
    lines.append(f"# Problem {pid}: {title}\n")
    lines.append(f"| Attribute | Detail |")
    lines.append(f"|-----------|--------|")
    lines.append(f"| **ID** | {pid} |")
    lines.append(f"| **Title** | {title} |")
    lines.append(f"| **Difficulty** | {difficulty} |")
    lines.append(f"| **Tags** | {', '.join(tags)} |")
    lines.append(f"| **Link** | [leetcode.com/problems/{slug}](https://leetcode.com/problems/{slug}/) |")
    lines.append("")

    # Description
    lines.append(description)
    lines.append("")
    lines.append("---\n")

    # Approach
    if approach:
        lines.append(f"## Approach: {pattern}\n")
        lines.append(approach)
        lines.append("")
    else:
        lines.append(f"## Pattern: {pattern}\n")

    # Pseudocode
    if pseudocode:
        lines.append("### Pseudo-code\n")
        lines.append("```")
        lines.append(pseudocode)
        lines.append("```\n")

    lines.append("---\n")

    # Mermaid
    if mermaid:
        lines.append("## Algorithm Flow\n")
        lines.append(mermaid)
        lines.append("")

    # Animation frames
    if animation:
        lines.append("## Visual State Transitions\n")
        lines.append(animation)
        lines.append("")

    # Walkthrough
    if walkthrough:
        lines.append("### Walkthrough\n")
        lines.append(walkthrough)
        lines.append("")

    lines.append("---\n")

    # Complexity
    lines.append("## Complexity Analysis\n")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| **Time** | {time_c} |")
    lines.append(f"| **Space** | {space_c} |")
    lines.append("")
    lines.append("---\n")

    # Solution code - Python
    lines.append("## Solution Code\n")
    lines.append("### Python3\n")
    lines.append("```python")
    lines.append(py_code)
    lines.append("```\n")

    # Solution code - C++
    lines.append("### C++\n")
    lines.append("```cpp")
    lines.append(cpp_code)
    lines.append("```\n")

    # Summary
    lines.append("### Summary\n")
    lines.append("| Aspect | Detail |")
    lines.append("|--------|--------|")
    lines.append(f"| **Pattern** | {pattern} |")
    lines.append(f"| **Time** | {time_c} |")
    lines.append(f"| **Space** | {space_c} |")
    lines.append("")
    lines.append("---\n---\n")

    return "\n".join(lines)


def generate_chapter_file(chapter_file, chapter_name, problems):
    """Generate a full chapter markdown file."""
    lines = []
    lines.append(f"# {chapter_name}\n")
    lines.append(f"> Chapter covering {len(problems)} problems related to **{chapter_name}**.\n")
    lines.append("")

    # Chapter TOC
    lines.append("## Problems in this Chapter\n")
    lines.append("| # | Problem | Difficulty | Pattern | Time | Space |")
    lines.append("|---|---------|------------|---------|------|-------|")
    for p in problems:
        pid = p["id"]
        sol = SOLUTIONS_KB.get(pid, {})
        auto = auto_generate_all(p.get("topic_tags", []))
        pattern = sol.get("pattern") or auto["pattern"]
        time_c = sol.get("time") or auto["time"]
        space_c = sol.get("space") or auto["space"]
        diff = p.get("difficulty", "")
        lines.append(f"| {pid} | [{p['title']}](#problem-{pid}-{sanitize_dirname(p['slug'])}) | {diff} | {pattern} | {time_c} | {space_c} |")
    lines.append("")
    lines.append("---\n---\n")

    # Each problem
    for p in problems:
        lines.append(generate_problem_section(p))

    return "\n".join(lines)


def generate_solution_file(prob):
    """Generate solution.py for a problem."""
    pid = prob["id"]
    title = prob["title"]
    difficulty = prob.get("difficulty", "Unknown")
    tags = prob.get("topic_tags", [])

    sol = SOLUTIONS_KB.get(pid, {})
    auto = auto_generate_all(tags)
    pattern = sol.get("pattern") or auto["pattern"]
    time_c = sol.get("time") or auto["time"]
    space_c = sol.get("space") or auto["space"]

    py_code, _, _, _, _, _ = _get_solutions(prob)

    docstring = f'"""\nProblem {pid}: {title}\n{"=" * (len(title) + 12)}\nDifficulty: {difficulty}\nTags: {", ".join(tags)}\nPattern: {pattern}\n\nTime Complexity:  {time_c}\nSpace Complexity: {space_c}\n"""\n\n'
    return docstring + py_code + "\n"


def generate_solution_cpp_file(prob):
    """Generate solution.cpp for a problem."""
    pid = prob["id"]
    title = prob["title"]
    difficulty = prob.get("difficulty", "Unknown")
    tags = prob.get("topic_tags", [])

    sol = SOLUTIONS_KB.get(pid, {})
    auto = auto_generate_all(tags)
    pattern = sol.get("pattern") or auto["pattern"]
    time_c = sol.get("time") or auto["time"]
    space_c = sol.get("space") or auto["space"]

    _, cpp_code, _, _, _, _ = _get_solutions(prob)

    header = f"/*\n * Problem {pid}: {title}\n * {'=' * (len(title) + 12)}\n * Difficulty: {difficulty}\n * Tags: {', '.join(tags)}\n * Pattern: {pattern}\n *\n * Time Complexity:  {time_c}\n * Space Complexity: {space_c}\n */\n\n"
    return header + cpp_code + "\n"


def generate_solution_md_file(prob):
    """Generate solution.md for a problem (per-problem detail file)."""
    pid = prob["id"]
    title = prob["title"]
    slug = prob["slug"]
    difficulty = prob.get("difficulty", "Unknown")
    tags = prob.get("topic_tags", [])
    content_html = prob.get("content", "")

    sol = SOLUTIONS_KB.get(pid, {})
    auto = auto_generate_all(tags, title)
    pattern = sol.get("pattern") or auto["pattern"]
    time_c = sol.get("time") or auto["time"]
    space_c = sol.get("space") or auto["space"]
    approach = sol.get("approach") or auto["approach"]
    pseudocode = sol.get("pseudocode") or auto["pseudocode"]
    mermaid = sol.get("mermaid") or auto["mermaid"]
    animation = sol.get("animation_frames") or auto["animation_frames"]

    py_code, cpp_code, _, _, _, _ = _get_solutions(prob)

    # Description
    is_premium = prob.get("paid_only", False) and not content_html
    description = strip_html_to_md(content_html)
    if not description:
        description = prob.get("content_text", "")
    if not description and is_premium:
        description = "*(Premium problem -- description requires LeetCode subscription)*"
    elif not description:
        description = "*(Description not available)*"

    lines = []
    lines.append(f"# Problem {pid}: {title}\n")
    lines.append(f"**Difficulty:** {difficulty}  ")
    lines.append(f"**Tags:** {', '.join(tags)}  ")
    lines.append(f"**Pattern:** {pattern}  ")
    lines.append(f"**Link:** [leetcode.com/problems/{slug}](https://leetcode.com/problems/{slug}/)\n")

    lines.append("## Description\n")
    lines.append(description)
    lines.append("")

    if approach:
        lines.append(f"## Approach: {pattern}\n")
        lines.append(approach)
        lines.append("")

    if pseudocode:
        lines.append("## Pseudocode\n")
        lines.append("```")
        lines.append(pseudocode)
        lines.append("```\n")

    if mermaid:
        lines.append("## Algorithm Flow\n")
        lines.append(mermaid)
        lines.append("")

    if animation:
        lines.append("## Visual State Transitions\n")
        lines.append(animation)
        lines.append("")

    lines.append("## Complexity Analysis\n")
    lines.append(f"- **Time:** {time_c}")
    lines.append(f"- **Space:** {space_c}")
    lines.append("")

    lines.append("## Solution (Python3)\n")
    lines.append("```python")
    lines.append(py_code)
    lines.append("```\n")

    lines.append("## Solution (C++)\n")
    lines.append("```cpp")
    lines.append(cpp_code)
    lines.append("```\n")

    return "\n".join(lines)


def generate_master_index(chapter_problems):
    """Generate the master solver.md index."""
    lines = []
    total_probs = sum(len(v) for v in chapter_problems.values())
    lines.append("# LeetCode Solver -- 2500 Problems Study Guide\n")
    lines.append(f"> A comprehensive DSA study guide covering {total_probs} LeetCode problems (ID 1-2500),")
    lines.append("> organized by topic/pattern. Each problem includes description, optimal approach,")
    lines.append("> mermaid algorithm flow, complexity analysis, and solutions in both Python3 and C++.\n")
    lines.append("")

    # Master TOC by chapter
    lines.append("## Chapters\n")
    lines.append("| # | Chapter | Problems | File |")
    lines.append("|---|---------|----------|------|")
    for idx, (ch_file, ch_name, _) in enumerate(CHAPTERS):
        probs = chapter_problems.get(ch_file, [])
        if probs:
            lines.append(f"| {idx+1} | **{ch_name}** | {len(probs)} | [solver/{ch_file}.md](solver/{ch_file}.md) |")
    lines.append("")

    # Full problem index
    lines.append("---\n")
    lines.append("## Complete Problem Index\n")
    lines.append("| ID | Problem | Difficulty | Chapter | Pattern |")
    lines.append("|----|---------|------------|---------|---------|")

    all_probs = []
    for ch_file, ch_name, _ in CHAPTERS:
        for p in chapter_problems.get(ch_file, []):
            sol = SOLUTIONS_KB.get(p["id"], {})
            auto = auto_generate_all(p.get("topic_tags", []))
            pat = sol.get("pattern") or auto["pattern"]
            all_probs.append((p["id"], p["title"], p.get("difficulty", ""), ch_name, pat))

    all_probs.sort(key=lambda x: x[0])
    for pid, title, diff, ch, pat in all_probs:
        lines.append(f"| {pid} | {title} | {diff} | {ch} | {pat} |")

    lines.append("")

    # Pattern cheat sheet
    lines.append("---\n")
    lines.append("## Pattern Cheat Sheet\n")
    lines.append("| Pattern | When to Use | Key Data Structure |")
    lines.append("|---------|-------------|---------------------|")
    lines.append("| **Hash Map Lookup** | Need O(1) lookup for complement/target | Dictionary / Set |")
    lines.append("| **Two Pointers** | Sorted array, pair finding, partitioning | Two index variables |")
    lines.append("| **Sliding Window** | Contiguous subarray/substring optimization | Window bounds + map |")
    lines.append("| **Fast and Slow Pointers** | Cycle detection, middle finding | Two-speed pointers |")
    lines.append("| **Binary Search** | Sorted data, search space reduction | Low/high bounds |")
    lines.append("| **BFS** | Shortest path, level-order traversal | Queue |")
    lines.append("| **DFS** | Tree/graph traversal, backtracking | Stack / Recursion |")
    lines.append("| **Dynamic Programming** | Overlapping subproblems, optimal substructure | DP table/memo |")
    lines.append("| **Greedy** | Local optimal leads to global optimal | Priority Queue / Sort |")
    lines.append("| **Backtracking** | Generate all combinations/permutations | Recursion + pruning |")
    lines.append("| **Union Find** | Connected components, cycle detection in undirected graph | Parent array |")
    lines.append("| **Topological Sort** | Dependency ordering, DAG processing | In-degree + queue |")
    lines.append("| **Trie** | Prefix matching, word search | Trie node tree |")
    lines.append("| **Monotonic Stack** | Next greater/smaller element | Stack |")
    lines.append("| **Interval Merge** | Overlapping intervals | Sort + sweep |")
    lines.append("")

    # File structure
    lines.append("---\n")
    lines.append("## File Structure\n")
    lines.append("```")
    lines.append("P1/")
    lines.append("  solver.md                        -- This file (master index)")
    lines.append("  solver/")
    for ch_file, ch_name, _ in CHAPTERS:
        lines.append(f"    {ch_file}.md")
    lines.append("  solutions/")
    lines.append("    problem_0001_two_sum/")
    lines.append("      solution.py           -- Python3 solution")
    lines.append("      solution.cpp          -- C++ solution")
    lines.append("      solution.md           -- Detailed writeup with mermaid")
    lines.append("    problem_0002_add_two_numbers/")
    lines.append("      solution.py")
    lines.append("      solution.cpp")
    lines.append("      solution.md")
    lines.append("    ...  (one directory per problem)")
    lines.append("```\n")

    return "\n".join(lines)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapters", type=str, default="all",
                        help="Which chapters to generate: 'all', '1-6', '7-12', '13-18'")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing files")
    args = parser.parse_args()

    # Load problem data
    if not CACHE_FILE.exists():
        print(f"ERROR: {CACHE_FILE} not found. Run fetch_problems.py first.")
        sys.exit(1)

    with open(CACHE_FILE) as f:
        data = json.load(f)

    problems = data.get("problems", [])
    print(f"Loaded {len(problems)} problems from cache")

    # Classify problems into chapters
    chapter_problems = {ch[0]: [] for ch in CHAPTERS}
    for prob in problems:
        ch = classify_problem(prob.get("topic_tags", []))
        chapter_problems[ch].append(prob)

    # Sort within each chapter
    for ch in chapter_problems:
        chapter_problems[ch].sort(key=lambda p: p["id"])

    # Determine which chapters to generate
    if args.chapters == "all":
        ch_range = range(len(CHAPTERS))
    elif args.chapters == "1-6":
        ch_range = range(0, 6)
    elif args.chapters == "7-12":
        ch_range = range(6, 12)
    elif args.chapters == "13-18":
        ch_range = range(12, 18)
    else:
        ch_range = range(len(CHAPTERS))

    # Create directories
    SOLVER_DIR.mkdir(parents=True, exist_ok=True)
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)

    # Generate chapter files
    for idx in ch_range:
        ch_file, ch_name, _ = CHAPTERS[idx]
        probs = chapter_problems.get(ch_file, [])
        if not probs:
            print(f"  Chapter {idx+1} ({ch_name}): no problems, skipping")
            continue

        out_path = SOLVER_DIR / f"{ch_file}.md"
        if out_path.exists() and not args.force:
            print(f"  Chapter {idx+1} ({ch_name}): {len(probs)} problems -- already exists, skipping (use --force)")
            continue

        print(f"  Chapter {idx+1} ({ch_name}): generating {len(probs)} problems...")
        content = generate_chapter_file(ch_file, ch_name, probs)
        out_path.write_text(content, encoding="utf-8")
        print(f"    -> {out_path} ({len(content)} chars)")

    # Generate solution.py, solution.cpp, solution.md files
    print("\nGenerating solution files (Python + C++ + Markdown)...")
    created_py = 0
    created_cpp = 0
    created_md = 0
    total = len(problems)
    for i, prob in enumerate(problems):
        pid = prob["id"]
        slug = prob["slug"]
        dirname = f"problem_{pid:04d}_{sanitize_dirname(slug)}"
        sol_dir = SOLUTIONS_DIR / dirname
        sol_dir.mkdir(parents=True, exist_ok=True)

        # solution.py
        py_file = sol_dir / "solution.py"
        if not py_file.exists() or args.force:
            py_file.write_text(generate_solution_file(prob), encoding="utf-8")
            created_py += 1

        # solution.cpp
        cpp_file = sol_dir / "solution.cpp"
        if not cpp_file.exists() or args.force:
            cpp_file.write_text(generate_solution_cpp_file(prob), encoding="utf-8")
            created_cpp += 1

        # solution.md
        md_file = sol_dir / "solution.md"
        if not md_file.exists() or args.force:
            md_file.write_text(generate_solution_md_file(prob), encoding="utf-8")
            created_md += 1

        if (i + 1) % 200 == 0:
            print(f"  Progress: {i+1}/{total} problems processed...")

    print(f"  Created {created_py} solution.py, {created_cpp} solution.cpp, {created_md} solution.md files")

    # Generate master index
    print("\nGenerating master solver.md...")
    index_content = generate_master_index(chapter_problems)
    index_path = PROJECT_DIR / "solver.md"
    index_path.write_text(index_content, encoding="utf-8")
    print(f"  -> {index_path} ({len(index_content)} chars)")

    print("\nDone!")


if __name__ == "__main__":
    main()
