"""
Problem 2231: Largest Number After Digit Swaps by Parity
======================================================
Difficulty: Easy
Tags: Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def largestInteger(self, num: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not num:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in num:
            heapq.heappush(heap, val)
            if len(heap) > (num if isinstance(num, int) else len(num)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
