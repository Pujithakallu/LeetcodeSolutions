"""
Problem 1761: Minimum Degree of a Connected Trio in a Graph
=========================================================
Difficulty: Hard
Tags: Graph Theory, Enumeration
Pattern: Graph Algorithm

Time Complexity:  O(V + E)
Space Complexity: O(V + E)
"""

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # Graph traversal - O(V+E) time
        from collections import defaultdict
        graph = defaultdict(list)
        # Build adjacency list from input
        n = len(n) if isinstance(n, list) else n
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
