"""
Problem 1857: Largest Color Value in a Directed Graph
===================================================
Difficulty: Hard
Tags: Hash Table, String, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Counting
Pattern: Topological Sort

Time Complexity:  O(V + E)
Space Complexity: O(V + E)
"""

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # Topological sort (Kahn's algorithm) - O(V+E)
        from collections import deque, defaultdict
        graph = defaultdict(list)
        n = colors if isinstance(colors, int) else len(colors)
        indegree = [0] * n
        # Build graph from prerequisites
        prereqs = edges if isinstance(edges, list) else colors
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
