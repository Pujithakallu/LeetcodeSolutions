"""
Problem 488: Zuma Game
=====================
Difficulty: Hard
Tags: String, Dynamic Programming, Stack, Breadth-First Search, Memoization
Pattern: BFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # BFS on graph - O(V+E) time
        from collections import deque
        if not board:
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
