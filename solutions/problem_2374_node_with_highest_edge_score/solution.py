"""
Problem 2374: Node With Highest Edge Score
========================================
Difficulty: Medium
Tags: Hash Table, Graph Theory
Pattern: Graph Algorithm

Time Complexity:  O(V + E)
Space Complexity: O(V + E)
"""

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        # Graph traversal - O(V+E) time
        from collections import defaultdict
        graph = defaultdict(list)
        # Build adjacency list from input
        n = len(edges) if isinstance(edges, list) else edges
        visited = [False] * n
        result = 0
        
        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                result += 1
        return result
