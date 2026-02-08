# Problem 36: Valid Sudoku

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Matrix  
**Pattern:** Hash Set  
**Link:** [leetcode.com/problems/valid-sudoku](https://leetcode.com/problems/valid-sudoku/)

## Description

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

	- Each row must contain the digits `1-9` without repetition.
	- Each column must contain the digits `1-9` without repetition.
	- Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

	- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
	- Only the filled cells need to be validated according to the mentioned rules.

 

Example 1:

```

**Input:** board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
**Output:** true

```

Example 2:

```

**Input:** board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
**Output:** false
**Explanation:** Same as Example 1, except with the **5** in the top left corner being modified to **8**. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

```

 

**Constraints:**

	- `board.length == 9`
	- `board[i].length == 9`
	- `board[i][j]` is a digit `1-9` or `'.'`.

## Approach: Hash Set

Track seen numbers in each row, column, and 3x3 box using sets.

## Pseudocode

```
1. Create sets for 9 rows, 9 cols, 9 boxes
2. For each cell: check row/col/box sets for duplicate
3. Add to sets if valid
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Init 9 row, col, box sets] --> B[For each cell i,j]
    B --> C{Already in row/col/box?}
    C -- Yes --> D[Return False]
    C -- No --> E[Add to sets]
    E --> B
```

## Complexity Analysis

- **Time:** O(1) (fixed 9x9 board)
- **Space:** O(1)

## Solution (Python3)

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                box_idx = (i // 3) * 3 + j // 3
                if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
        return True
```

## Solution (C++)

```cpp
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<string>>& board) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < board.size(); i++) {
            int complement = board - board[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[board[i]] = i;
        }
        return false;
    }
};
```
