# Problem 22: Generate Parentheses

**Difficulty:** Medium  
**Tags:** String, Dynamic Programming, Backtracking  
**Pattern:** Backtracking  
**Link:** [leetcode.com/problems/generate-parentheses](https://leetcode.com/problems/generate-parentheses/)

## Description

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

 

Example 1:

```
**Input:** n = 3
**Output:** ["((()))","(()())","(())()","()(())","()()()"]

```
Example 2:

```
**Input:** n = 1
**Output:** ["()"]

```

 

**Constraints:**

	- `1 <= n <= 8`

## Approach: Backtracking

Backtrack with two counters: open and close. Add '(' if open < n. Add ')' if close < open.

## Pseudocode

```
1. backtrack(path, open, close):
   If len==2n: add to result
   If open < n: try '('
   If close < open: try ')'
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Start: open=0, close=0] --> B{Length == 2n?}
    B -- Yes --> C[Add to result]
    B -- No --> D{open < n?}
    D -- Yes --> E["Add '(' recurse"]
    D --> F{close < open?}
    F -- Yes --> G["Add ')' recurse"]
```

## Visual State Transitions

**Backtracking Decision Tree:**

**Frame 1: Root - start with empty path**
```mermaid
graph TD
    R["[] choices: 1,2,3"]
    R --- A["[1]"]
    R --- B["[2]"]
    R --- C["[3]"]
```

**Frame 2: Explore branch [1]**
```mermaid
graph TD
    R["[]"]
    R --- A["[1]"]
    A --- A1["[1,2]"]
    A --- A2["[1,3]"]
    A1 --- A1a["[1,2,3] SOLUTION"]
    R --- B["[2] ..."]
    R --- C["[3] ..."]
```

**Frame 3: Backtrack, explore [2]**
```mermaid
graph TD
    R["[]"]
    R --- A["[1] done"]
    R --- B["[2]"]
    B --- B1["[2,1]"]
    B --- B2["[2,3]"]
    B1 --- B1a["[2,1,3] SOLUTION"]
    R --- C["[3] ..."]
```

**Frame 4: All solutions found**
```mermaid
graph TD
    R["Complete: 6 permutations found"]
    R --- S1["[1,2,3]"]
    R --- S2["[1,3,2]"]
    R --- S3["[2,1,3] ..."]
```


## Complexity Analysis

- **Time:** O(4^n / sqrt(n))
- **Space:** O(n)

## Solution (Python3)

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(path, open_count, close_count):
            if len(path) == 2 * n:
                result.append(''.join(path))
                return
            if open_count < n:
                path.append('(')
                backtrack(path, open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(')')
                backtrack(path, open_count, close_count + 1)
                path.pop()
        backtrack([], 0, 0)
        return result
```

## Solution (C++)

```cpp
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)n.size(); i++) {
                path.push_back(n[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
```
