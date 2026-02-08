# Problem 1591: Strange Printer II

**Difficulty:** Hard  
**Tags:** Array, Graph Theory, Topological Sort, Matrix  
**Pattern:** Topological Sort  
**Link:** [leetcode.com/problems/strange-printer-ii](https://leetcode.com/problems/strange-printer-ii/)

## Description

There is a strange printer with the following two special requirements:

	- On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
	- Once the printer has used a color for the above operation, **the same color cannot be used again**.

You are given a `m x n` matrix `targetGrid`, where `targetGrid[row][col]` is the color in the position `(row, col)` of the grid.

Return `true`* if it is possible to print the matrix *`targetGrid`*,** otherwise, return *`false`.

 

Example 1:

```

**Input:** targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
**Output:** true

```

Example 2:

```

**Input:** targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
**Output:** true

```

Example 3:

```

**Input:** targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
**Output:** false
**Explanation:** It is impossible to form targetGrid because it is not allowed to print the same color in different turns.

```

 

**Constraints:**

	- `m == targetGrid.length`
	- `n == targetGrid[i].length`
	- `1 <= m, n <= 60`
	- `1 <= targetGrid[row][col] <= 60`

## Approach: Topological Sort

Order nodes in a DAG so every edge u->v has u before v. Use Kahn's algorithm (BFS with in-degree tracking) or DFS-based ordering.

## Pseudocode

```
1. Compute in-degree for every node
2. Enqueue all nodes with in-degree 0
3. While queue not empty:
   a. Dequeue node u, add to result order
   b. For each neighbor v of u:
      - Decrease in-degree of v
      - If in-degree becomes 0: enqueue v
4. If result size != V: cycle exists
5. Return topological order
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Compute in-degree for each node] --> B[Enqueue nodes with in-degree 0]
    B --> C{Queue not empty?}
    C -- Yes --> D[Dequeue node u]
    D --> E[Add u to result order]
    E --> F[For each neighbor v of u]
    F --> G[in-degree_v -= 1]
    G --> H{in-degree_v == 0?}
    H -- Yes --> I[Enqueue v]
    H -- No --> F
    I --> F
    F --> C
    C -- No --> J{Result size == V?}
    J -- Yes --> K[Return topological order]
    J -- No --> L[Cycle detected]
```

## Visual State Transitions

**Topological Sort (Kahn's Algorithm):**

**Frame 1: Compute in-degrees**
```mermaid
graph LR
    A(("A in=0")) --> B(("B in=1"))
    A --> C(("C in=1"))
    B --> D(("D in=2"))
    C --> D
    Q["Queue: [A] (in-degree 0)"]
```

**Frame 2: Process A, reduce neighbors**
```mermaid
graph LR
    A(("A DONE"))
    B(("B in=0"))
    C(("C in=0"))
    D(("D in=2"))
    Q["Order: [A], Queue: [B, C]"]
```

**Frame 3: Process B and C**
```mermaid
graph LR
    A(("A DONE"))
    B(("B DONE"))
    C(("C DONE"))
    D(("D in=0"))
    Q["Order: [A,B,C], Queue: [D]"]
```

**Frame 4: Complete**
```mermaid
graph LR
    A(("A")) --> B(("B")) --> D(("D"))
    A --> C(("C")) --> D
    R["Topological Order: A, B, C, D"]
```


## Complexity Analysis

- **Time:** O(V + E)
- **Space:** O(V + E)

## Solution (Python3)

```python
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        # Topological sort (Kahn's algorithm) - O(V+E)
        from collections import deque, defaultdict
        graph = defaultdict(list)
        n = targetGrid if isinstance(targetGrid, int) else len(targetGrid)
        indegree = [0] * n
        # Build graph from prerequisites
        prereqs = targetGrid if isinstance(targetGrid, list) else targetGrid
        for edge in prereqs:
            if isinstance(edge, (list, tuple)) and len(edge) >= 2:
                graph[edge[1]].append(edge[0])
                indegree[edge[0]] += 1
        queue = deque([i for i in range(n) if indegree[i] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return len(order) == n if isinstance(False, bool) else order
```

## Solution (C++)

```cpp
#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isPrintable(vector<vector<int>>& targetGrid) {
        // Topological sort (Kahn's) - O(V+E)
        int n = targetGrid;
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        for (auto& edge : targetGrid) {
            graph[edge[1]].push_back(edge[0]);
            indegree[edge[0]]++;
        }
        queue<int> q;
        for (int i = 0; i < n; i++)
            if (indegree[i] == 0) q.push(i);
        vector<int> order;
        while (!q.empty()) {
            int node = q.front(); q.pop();
            order.push_back(node);
            for (int neighbor : graph[node]) {
                if (--indegree[neighbor] == 0) q.push(neighbor);
            }
        }
        return order.size() == n;
    }
};
```
