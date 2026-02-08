# Problem 542: 01 Matrix

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Breadth-First Search, Matrix  
**Pattern:** BFS on Matrix / Grid  
**Link:** [leetcode.com/problems/01-matrix](https://leetcode.com/problems/01-matrix/)

## Description

Given an `m x n` binary matrix `mat`, return *the distance of the nearest *`0`* for each cell*.

The distance between two cells sharing a common edge is `1`.

 

Example 1:

```

**Input:** mat = [[0,0,0],[0,1,0],[0,0,0]]
**Output:** [[0,0,0],[0,1,0],[0,0,0]]

```

Example 2:

```

**Input:** mat = [[0,0,0],[0,1,0],[1,1,1]]
**Output:** [[0,0,0],[0,1,0],[1,2,1]]

```

 

**Constraints:**

	- `m == mat.length`
	- `n == mat[i].length`
	- `1 <= m, n <= 10^4`
	- `1 <= m * n <= 10^4`
	- `mat[i][j]` is either `0` or `1`.
	- There is at least one `0` in `mat`.

 

**Note:** This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/

## Approach: BFS on Matrix / Grid

Breadth-first search on the grid. Enqueue all starting cells, then expand level by level. BFS on grids finds shortest distance from source(s).

## Pseudocode

```
1. Enqueue all source cells, mark visited
2. distance = 0
3. While queue not empty:
   a. Process all cells at current distance
   b. For each cell, enqueue unvisited neighbors
   c. distance++
4. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Enqueue source cells] --> B{Queue not empty?}
    B -- Yes --> C[Process current level]
    C --> D[For each cell in level]
    D --> E[Check 4 neighbors]
    E --> F{Valid and unvisited?}
    F -- Yes --> G[Mark visited, enqueue]
    F -- No --> E
    G --> E
    D --> H[distance++]
    H --> B
    B -- No --> I[Return distances]
```

## Visual State Transitions

**Multi-source BFS on Grid:**

**Frame 1: Enqueue all sources**
```mermaid
graph TD
    subgraph Grid
        R0["S  .  ."]
        R1[".  .  ."]
        R2[".  .  S"]
    end
    Q["Queue: [(0,0), (2,2)], dist=0"]
```

**Frame 2: Expand distance 1**
```mermaid
graph TD
    subgraph Grid
        R0["0  1  ."]
        R1["1  .  1"]
        R2[".  1  0"]
    end
    Q["Distance 1 cells processed"]
```

**Frame 3: Expand distance 2**
```mermaid
graph TD
    subgraph Grid
        R0["0  1  2"]
        R1["1  2  1"]
        R2["2  1  0"]
    end
    Q["All cells reached. Max distance = 2"]
```


## Complexity Analysis

- **Time:** O(m * n)
- **Space:** O(m * n)

## Solution (Python3)

```python
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS on grid - O(m*n) time
        from collections import deque
        if not mat:
            return []
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        visited = set()
        # Initialize BFS sources
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 or mat[r][c] == '1':
                    queue.append((r, c, 0))
                    visited.add((r, c))
        steps = 0
        while queue:
            r, c, d = queue.popleft()
            steps = max(steps, d)
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, d+1))
        return steps
```

## Solution (C++)

```cpp
#include <algorithm>
#include <queue>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        // BFS on grid - O(m*n) time
        if (mat.empty()) return {};
        int rows = mat.size(), cols = mat[0].size();
        queue<tuple<int,int,int>> q;
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (mat[r][c] == 1) {
                    q.push({r, c, 0});
                    visited[r][c] = true;
                }
        int steps = 0;
        while (!q.empty()) {
            auto [r, c, d] = q.front(); q.pop();
            steps = max(steps, d);
            for (auto& dir : dirs) {
                int nr = r+dir[0], nc = c+dir[1];
                if (nr>=0 && nr<rows && nc>=0 && nc<cols && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.push({nr, nc, d+1});
                }
            }
        }
        return steps;
    }
};
```
