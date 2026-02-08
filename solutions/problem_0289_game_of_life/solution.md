# Problem 289: Game of Life

**Difficulty:** Medium  
**Tags:** Array, Matrix, Simulation  
**Pattern:** Simulation  
**Link:** [leetcode.com/problems/game-of-life](https://leetcode.com/problems/game-of-life/)

## Description

According to Wikipedia's article: "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: **live** (represented by a `1`) or **dead** (represented by a `0`). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

	- Any live cell with fewer than two live neighbors dies as if caused by under-population.
	- Any live cell with two or three live neighbors lives on to the next generation.
	- Any live cell with more than three live neighbors dies, as if by over-population.
	- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the `m x n` grid `board`. In this process, births and deaths occur **simultaneously**.

Given the current state of the `board`, **update** the `board` to reflect its next state.

**Note** that you do not need to return anything.

 

Example 1:

```

**Input:** board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
**Output:** [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

```

Example 2:

```

**Input:** board = [[1,1],[1,0]]
**Output:** [[1,1],[1,1]]

```

 

**Constraints:**

	- `m == board.length`
	- `n == board[i].length`
	- `1 <= m, n <= 25`
	- `board[i][j]` is `0` or `1`.

 

**Follow up:**

	- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
	- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

## Approach: Simulation

Simulate the process described in the problem step by step. Follow the rules exactly, tracking state at each step.

## Pseudocode

```
1. Initialize state (grid, pointers, counters)
2. For each step / iteration:
   a. Apply the transformation rules
   b. Update state
   c. Check termination condition
3. Return final state or result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Initialize state] --> B[Apply transformation rules]
    B --> C[Update state]
    C --> D{Termination condition?}
    D -- No --> B
    D -- Yes --> E[Return final state]
```

## Complexity Analysis

- **Time:** O(n) or O(n * k)
- **Space:** O(n)

## Solution (Python3)

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # Simulation approach - follow the rules step by step
        result = None
        for i in range(len(board) if isinstance(board, list) else board):
            # Simulate each step
            pass
        return result
```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        // Simulation approach
        int n = board.size();
        for (int i = 0; i < n; i++) {
            // Simulate each step
        }
        return ;
    }
};
```
