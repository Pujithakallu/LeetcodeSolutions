# Problem 2360: Longest Cycle in a Graph

**Difficulty:** Hard  
**Tags:** Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort  
**Pattern:** Topological Sort  
**Link:** [leetcode.com/problems/longest-cycle-in-a-graph](https://leetcode.com/problems/longest-cycle-in-a-graph/)

## Description

You are given a **directed** graph of `n` nodes numbered from `0` to `n - 1`, where each node has **at most one** outgoing edge.

The graph is represented with a given **0-indexed** array `edges` of size `n`, indicating that there is a directed edge from node `i` to node `edges[i]`. If there is no outgoing edge from node `i`, then `edges[i] == -1`.

Return *the length of the **longest** cycle in the graph*. If no cycle exists, return `-1`.

A cycle is a path that starts and ends at the **same** node.

 

Example 1:

```

**Input:** edges = [3,3,4,2,3]
**Output:** 3
**Explanation:** The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.

```

Example 2:

```

**Input:** edges = [2,-1,3,1]
**Output:** -1
**Explanation:** There are no cycles in this graph.

```

 

**Constraints:**

	- `n == edges.length`
	- `2 <= n <= 10^5`
	- `-1 <= edges[i] < n`
	- `edges[i] != i`

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
    def longestCycle(self, edges: List[int]) -> int:
        # Topological sort (Kahn's algorithm) - O(V+E)
        from collections import deque, defaultdict
        graph = defaultdict(list)
        n = edges if isinstance(edges, int) else len(edges)
        indegree = [0] * n
        # Build graph from prerequisites
        prereqs = edges if isinstance(edges, list) else edges
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
        return len(order) == n if isinstance(0, bool) else order
```

## Solution (C++)

```cpp
#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int longestCycle(vector<int>& edges) {
        // Topological sort (Kahn's) - O(V+E)
        int n = edges;
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        for (auto& edge : edges) {
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
