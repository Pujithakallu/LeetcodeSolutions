
# Agent Instructions: LeetCode Automation & Solver

## 1. Objective
You are an expert software engineer agent. Your goal is to solve the first 10 LeetCode problems autonomously. You will handle the entire lifecycle: scraping, pattern recognition, visualization, implementation, and live validation. Interested in generating a markdown file with the first 10 solutions for leetcode that can help students to brush DSA
---

## 2. Phase 1: Browser Setup & Authentication
1. **Tooling:** Use `playwright` (Python) to automate the browser. (You are the expert in scraping. You can pick the other state of art tools).
2. **Login:** - Navigate to `https://leetcode.com/accounts/login/`.
   - Use provided credentials (Username/Password) to authenticate.
   - Please find the login details:
     Username: XXXXXXX@gmail.com
     Password: XXXXX
     You need to click on "Verify You are Human" as specified in attached image.
     https://leetcode.com/problemset/ ====> LIST OF ALL PROBLEMS
     https://leetcode.com/problems/two-sum/description/  ===> FIRST PROBLEM
   - **Persistence:** Save the browser state to `auth.json` to avoid repeated logins and CAPTCHA triggers.

---

## 3. Phase 2: The Problem-Solving Loop (Repeat for Problems 1-10)

### Step A: Scraping & Context Gathering
- Navigate to the problem URL.
- **Extract:** - Problem title and description.
    - Constraints (e.g., $N \le 10^5$).
    - Example inputs and outputs.
    - The starter code template (Python3).

### Step B: Strategic Analysis
- **Identify Pattern:** Determine the optimal algorithmic pattern (e.g., Two Pointers, Sliding Window, Greedy, etc.).
- **Complexity Target:** Based on constraints, define the target Time and Space complexity.
- **Pseudo-code:** Write a clear, step-by-step logic plan.
- **Visualization:** Create a **Mermaid.js** diagram to explain the algorithm's flow to a student.

### Step C: Implementation
- Create a directory: `solutions/problem_[ID]_[Name]/`.
- Create `solution.py` with the optimized code.
- **Documentation:** Include a docstring at the top of the file summarizing:
    - **Time Complexity:** $O(...)$
    - **Space Complexity:** $O(...)$

### Step D: Live Validation (Submission)
- Use Playwright to:
    1. Paste the solution into the LeetCode web editor.
    2. Click the **"Submit"** button.
    3. Monitor the DOM for the result (e.g., "Accepted", "Wrong Answer", or "TLE").

### Step E: Failure Analysis & Iteration
- **If "Accepted":** Move to the next problem.
- **If Failure:**
    1. Scrape the "Last Executed Input" and "Expected vs. Output" data.
    2. Create/Update a `debugging.md` file in the problem folder.
    3. Analyze the logic flaw (e.g., "Edge case for empty array not handled").
    4. Refactor the code and re-submit.

---

## 4. Final Deliverables (Per Problem)
The following files must exist in each problem folder:
1. `solution.py`: The final, verified Python code.
2. `explanation.md`: 
    - Problem description.
    - Mermaid diagram logic.
    - Complexity analysis.
    - A summary of the pattern used.
3. `status.log`: A log of submission attempts and results.

---

## 5. Execution Rules
- **Optimality:** Do not provide brute-force solutions unless they are the only viable option.
- **Clarity:** Ensure code is PEP 8 compliant.
- **Scannability:** Use Markdown tables and bold text in explanations for high readability.
