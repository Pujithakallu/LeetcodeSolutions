"""
Problem 1591: Strange Printer II
==============================
Difficulty: Hard
Tags: Array, Graph Theory, Topological Sort, Matrix
Pattern: Topological Sort

Time Complexity:  O(V + E)
Space Complexity: O(V + E)
"""

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
