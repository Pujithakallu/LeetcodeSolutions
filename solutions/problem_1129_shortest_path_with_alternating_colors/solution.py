"""
Problem 1129: Shortest Path with Alternating Colors
=================================================
Difficulty: Medium
Tags: Breadth-First Search, Graph Theory
Pattern: BFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # BFS on graph - O(V+E) time
        from collections import deque
        if not n:
            return []
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
