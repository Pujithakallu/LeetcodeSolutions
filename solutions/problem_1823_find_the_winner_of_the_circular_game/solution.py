"""
Problem 1823: Find the Winner of the Circular Game
================================================
Difficulty: Medium
Tags: Array, Math, Recursion, Queue, Simulation
Pattern: Queue / BFS

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Queue-based approach - O(n) time
        from collections import deque
        queue = deque()
        for val in n:
            queue.append(val)
        result = []
        while queue:
            result.append(queue.popleft())
        return result
