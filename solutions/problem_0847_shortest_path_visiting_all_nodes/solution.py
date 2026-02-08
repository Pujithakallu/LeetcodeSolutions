"""
Problem 847: Shortest Path Visiting All Nodes
============================================
Difficulty: Hard
Tags: Dynamic Programming, Bit Manipulation, Breadth-First Search, Graph Theory, Bitmask
Pattern: BFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # BFS on graph - O(V+E) time
        from collections import deque
        if not graph:
            return 0
        visited = set()
        queue = deque([0])
        visited.add(0)
        dist = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                # Process node
            dist += 1
        return dist
