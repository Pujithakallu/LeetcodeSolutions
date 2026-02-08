# Problem 52: N-Queens II

**Difficulty:** Hard  
**Tags:** Backtracking  
**Pattern:** Backtracking  
**Link:** [leetcode.com/problems/n-queens-ii](https://leetcode.com/problems/n-queens-ii/)

## Description

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *the number of distinct solutions to the **n-queens puzzle***.

 

Example 1:

```

**Input:** n = 4
**Output:** 2
**Explanation:** There are two distinct solutions to the 4-queens puzzle as shown.

```

Example 2:

```

**Input:** n = 1
**Output:** 1

```

 

**Constraints:**

	- `1 <= n <= 9`

## Approach: Backtracking

Same as N-Queens I but just count solutions instead of storing boards.

## Pseudocode

```
Same as N-Queens but increment counter instead of recording
```

## Algorithm Flow

```mermaid
flowchart TD
    A["backtrack(path, choices)"] --> B{Path complete?}
    B -- Yes --> C[Add path to results]
    B -- No --> D[For each valid choice]
    D --> E[Add choice to path]
    E --> F["backtrack(path, remaining)"]
    F --> G[Remove choice from path]
    G --> D
    D --> H{All choices tried}
    H --> I[Return]
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

- **Time:** O(n!)
- **Space:** O(n)

## Solution (Python3)

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        cols, d1, d2 = set(), set(), set()
        def solve(row):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if col in cols or row-col in d1 or row+col in d2:
                    continue
                cols.add(col); d1.add(row-col); d2.add(row+col)
                solve(row+1)
                cols.discard(col); d1.discard(row-col); d2.discard(row+col)
        solve(0)
        return self.count
```

## Solution (C++)

```cpp
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int totalNQueens(int n) {
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
