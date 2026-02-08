"""
Problem 329: Longest Increasing Path in a Matrix
===============================================
Difficulty: Hard
Tags: Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix
Pattern: Topological Sort

Time Complexity:  O(V + E)
Space Complexity: O(V + E)
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Topological sort (Kahn's algorithm) - O(V+E)
        from collections import deque, defaultdict
        graph = defaultdict(list)
        n = matrix if isinstance(matrix, int) else len(matrix)
        indegree = [0] * n
        # Build graph from prerequisites
        prereqs = matrix if isinstance(matrix, list) else matrix
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
