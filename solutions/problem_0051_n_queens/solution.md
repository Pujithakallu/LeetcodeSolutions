# Problem 51: N-Queens

**Difficulty:** Hard  
**Tags:** Array, Backtracking  
**Pattern:** Backtracking  
**Link:** [leetcode.com/problems/n-queens](https://leetcode.com/problems/n-queens/)

## Description

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

 

Example 1:

```

**Input:** n = 4
**Output:** [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
**Explanation:** There exist two distinct solutions to the 4-queens puzzle as shown above

```

Example 2:

```

**Input:** n = 1
**Output:** [["Q"]]

```

 

**Constraints:**

	- `1 <= n <= 9`

## Approach: Backtracking

Place queens row by row. Track attacked columns and diagonals with sets.

## Pseudocode

```
1. For each row: try each column
2. Skip if column/diagonal attacked
3. Place queen, recurse to next row
4. Backtrack if no solution
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Start row 0] --> B[Try each column]
    B --> C{Column/diagonal free?}
    C -- Yes --> D[Place queen]
    D --> E[Recurse next row]
    C -- No --> F[Next column]
    E --> G{All rows filled?}
    G -- Yes --> H[Record solution]
    G -- No --> I[Backtrack]
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
- **Space:** O(n^2)

## Solution (Python3)

```python
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [['.' ] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
                cols.discard(col)
                diag1.discard(row - col)
                diag2.discard(row + col)
        backtrack(0)
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
    vector<vector<string>> solveNQueens(int n) {
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
