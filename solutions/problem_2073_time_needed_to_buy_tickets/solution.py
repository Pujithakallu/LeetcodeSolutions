"""
Problem 2073: Time Needed to Buy Tickets
======================================
Difficulty: Easy
Tags: Array, Queue, Simulation
Pattern: Queue / BFS

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Queue-based approach - O(n) time
        from collections import deque
        queue = deque()
        for val in tickets:
            queue.append(val)
        result = []
        while queue:
            result.append(queue.popleft())
        return result
