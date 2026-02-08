"""
Problem 378: Kth Smallest Element in a Sorted Matrix
===================================================
Difficulty: Medium
Tags: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not matrix:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in matrix:
            heapq.heappush(heap, val)
            if len(heap) > (k if isinstance(k, int) else len(matrix)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
