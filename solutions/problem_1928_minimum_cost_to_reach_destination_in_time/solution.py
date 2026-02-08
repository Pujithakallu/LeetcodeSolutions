"""
Problem 1928: Minimum Cost to Reach Destination in Time
=====================================================
Difficulty: Hard
Tags: Array, Dynamic Programming, Graph Theory
Pattern: Graph Algorithm

Time Complexity:  O(V + E)
Space Complexity: O(V + E)
"""

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # Graph traversal - O(V+E) time
        from collections import defaultdict
        graph = defaultdict(list)
        # Build adjacency list from input
        n = len(maxTime) if isinstance(maxTime, list) else maxTime
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
