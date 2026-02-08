# Problem 463: Island Perimeter

**Difficulty:** Easy  
**Tags:** Array, Depth-First Search, Breadth-First Search, Matrix  
**Pattern:** DFS on Matrix / Grid  
**Link:** [leetcode.com/problems/island-perimeter](https://leetcode.com/problems/island-perimeter/)

## Description

You are given `row x col` `grid` representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water.

Grid cells are connected **horizontally/vertically** (not diagonally). The `grid` is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:

```

**Input:** grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
**Output:** 16
**Explanation:** The perimeter is the 16 yellow stripes in the image above.

```

Example 2:

```

**Input:** grid = [[1]]
**Output:** 4

```

Example 3:

```

**Input:** grid = [[1,0]]
**Output:** 4

```

 

**Constraints:**

	- `row == grid.length`
	- `col == grid[i].length`
	- `1 <= row, col <= 100`
	- `grid[i][j]` is `0` or `1`.
	- There is exactly one island in `grid`.

## Approach: DFS on Matrix / Grid

Treat the grid as a graph where each cell connects to its 4 (or 8) neighbors. DFS from target cells, marking visited to avoid revisiting.

## Pseudocode

```
1. For each cell (r, c) in grid:
   a. If cell meets start condition:
      - Call dfs(r, c)
2. dfs(r, c):
   a. If out of bounds or visited or invalid: return
   b. Mark cell visited
   c. Recurse on 4 neighbors: up, down, left, right
3. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[For each cell in grid] --> B{Matches start condition?}
    B -- Yes --> C["dfs(r, c)"]
    B -- No --> A
    C --> D{Out of bounds or visited?}
    D -- Yes --> E[Return]
    D -- No --> F[Mark visited, process cell]
    F --> G["dfs(r+1,c), dfs(r-1,c)"]
    G --> H["dfs(r,c+1), dfs(r,c-1)"]
    H --> I[Return result]
```

## Visual State Transitions

**DFS on Grid (Island/Flood Fill):**

**Frame 1: Find first land cell**
```mermaid
graph TD
    subgraph Grid
        R0["1  1  0"]
        R1["1  0  0"]
        R2["0  0  1"]
    end
    S["Start DFS at (0,0)"]
```

**Frame 2: DFS explores connected cells**
```mermaid
graph TD
    subgraph Grid
        R0["V  1  0"]
        R1["1  0  0"]
        R2["0  0  1"]
    end
    S["Visited (0,0), explore neighbors"]
```

**Frame 3: Mark entire island**
```mermaid
graph TD
    subgraph Grid
        R0["V  V  0"]
        R1["V  0  0"]
        R2["0  0  1"]
    end
    S["Island 1 complete, area=3"]
```

**Frame 4: Find second island**
```mermaid
graph TD
    subgraph Grid
        R0["V  V  0"]
        R1["V  0  0"]
        R2["0  0  V"]
    end
    S["Island 2 at (2,2), area=1. Total=2 islands"]
```


## Complexity Analysis

- **Time:** O(m * n)
- **Space:** O(m * n)

## Solution (Python3)

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # DFS on grid - O(m*n) time
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == '0' or grid[r][c] == 0:
                return
            grid[r][c] = '0'
            dfs(r+1, c); dfs(r-1, c)
            dfs(r, c+1); dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' or grid[r][c] == 1:
                    dfs(r, c)
                    count += 1
        return count
```

## Solution (C++)

```cpp
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        // DFS on grid - O(m*n) time
        if (grid.empty()) return 0;
        int rows = grid.size(), cols = grid[0].size();
        int count = 0;
        function<void(int, int)> dfs = [&](int r, int c) {
            if (r < 0 || r >= rows || c < 0 || c >= cols) return;
            if (grid[r][c] == '0') return;
            grid[r][c] = '0';
            dfs(r+1, c); dfs(r-1, c);
            dfs(r, c+1); dfs(r, c-1);
        };
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    dfs(r, c);
                    count++;
                }
            }
        }
        return count;
    }
};
```
