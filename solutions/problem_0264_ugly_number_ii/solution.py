"""
Problem 264: Ugly Number II
==========================
Difficulty: Medium
Tags: Hash Table, Math, Dynamic Programming, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not n:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in n:
            heapq.heappush(heap, val)
            if len(heap) > (n if isinstance(n, int) else len(n)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
