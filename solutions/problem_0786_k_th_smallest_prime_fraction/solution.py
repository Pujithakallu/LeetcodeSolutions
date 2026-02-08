"""
Problem 786: K-th Smallest Prime Fraction
========================================
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not arr:
            return []
        # Min heap (negate for max heap)
        heap = []
        for val in arr:
            heapq.heappush(heap, val)
            if len(heap) > (k if isinstance(k, int) else len(arr)):
                heapq.heappop(heap)
        return heap[0] if heap else []
