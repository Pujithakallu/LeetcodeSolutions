"""
Problem 703: Kth Largest Element in a Stream
===========================================
Difficulty: Easy
Tags: Tree, Design, Binary Search Tree, Heap (Priority Queue), Binary Tree, Data Stream
Pattern: Heap / Design

Time Complexity:  O(log k) per add
Space Complexity: O(k)
"""

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
