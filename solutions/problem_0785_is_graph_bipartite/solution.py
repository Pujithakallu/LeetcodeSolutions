"""
Problem 785: Is Graph Bipartite?
===============================
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
Pattern: BFS / Graph Coloring

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

from collections import deque

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        for start in range(n):
            if color[start] != -1:
                continue
            queue = deque([start])
            color[start] = 0
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
        return True
