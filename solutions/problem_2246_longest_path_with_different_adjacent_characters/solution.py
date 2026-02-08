"""
Problem 2246: Longest Path With Different Adjacent Characters
===========================================================
Difficulty: Hard
Tags: Array, String, Tree, Depth-First Search, Graph Theory, Topological Sort
Pattern: Topological Sort

Time Complexity:  O(V + E)
Space Complexity: O(V + E)
"""

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # Topological sort (Kahn's algorithm) - O(V+E)
        from collections import deque, defaultdict
        graph = defaultdict(list)
        n = parent if isinstance(parent, int) else len(parent)
        indegree = [0] * n
        # Build graph from prerequisites
        prereqs = s if isinstance(s, list) else parent
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
