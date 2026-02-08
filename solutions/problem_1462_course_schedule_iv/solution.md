# Problem 1462: Course Schedule IV

**Difficulty:** Medium  
**Tags:** Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort  
**Pattern:** Topological Sort  
**Link:** [leetcode.com/problems/course-schedule-iv](https://leetcode.com/problems/course-schedule-iv/)

## Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `ai` first if you want to take course `bi`.

	- For example, the pair `[0, 1]` indicates that you have to take course `0` before you can take course `1`.

Prerequisites can also be **indirect**. If course `a` is a prerequisite of course `b`, and course `b` is a prerequisite of course `c`, then course `a` is a prerequisite of course `c`.

You are also given an array `queries` where `queries[j] = [uj, vj]`. For the `j^th` query, you should answer whether course `uj` is a prerequisite of course `vj` or not.

Return *a boolean array *`answer`*, where *`answer[j]`* is the answer to the *`j^th`* query.*

 

Example 1:

```

**Input:** numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
**Output:** [false,true]
**Explanation:** The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

```

Example 2:

```

**Input:** numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
**Output:** [false,false]
**Explanation:** There are no prerequisites, and each course is independent.

```

Example 3:

```

**Input:** numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
**Output:** [true,true]

```

 

**Constraints:**

	- `2 <= numCourses <= 100`
	- `0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)`
	- `prerequisites[i].length == 2`
	- `0 <= ai, bi <= numCourses - 1`
	- `ai != bi`
	- All the pairs `[ai, bi]` are **unique**.
	- The prerequisites graph has no cycles.
	- `1 <= queries.length <= 10^4`
	- `0 <= ui, vi <= numCourses - 1`
	- `ui != vi`

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
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Topological sort (Kahn's algorithm) - O(V+E)
        from collections import deque, defaultdict
        graph = defaultdict(list)
        n = numCourses if isinstance(numCourses, int) else len(numCourses)
        indegree = [0] * n
        # Build graph from prerequisites
        prereqs = prerequisites if isinstance(prerequisites, list) else numCourses
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
        return len(order) == n if isinstance([], bool) else order
```

## Solution (C++)

```cpp
#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        // Topological sort (Kahn's) - O(V+E)
        int n = numCourses;
        vector<vector<int>> graph(n);
        vector<int> indegree(n, 0);
        for (auto& edge : prerequisites) {
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
