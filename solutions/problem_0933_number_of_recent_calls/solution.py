"""
Problem 933: Number of Recent Calls
==================================
Difficulty: Easy
Tags: Design, Queue, Data Stream
Pattern: Queue / Design

Time Complexity:  O(1) amortized
Space Complexity: O(n)
"""

from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
