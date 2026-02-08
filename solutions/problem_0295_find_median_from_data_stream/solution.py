"""
Problem 295: Find Median from Data Stream
========================================
Difficulty: Hard
Tags: Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream
Pattern: Two Heaps / Design

Time Complexity:  O(log n) add, O(1) find
Space Complexity: O(n)
"""

import heapq

class Solution:
    pass

class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (negated)
        self.hi = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
