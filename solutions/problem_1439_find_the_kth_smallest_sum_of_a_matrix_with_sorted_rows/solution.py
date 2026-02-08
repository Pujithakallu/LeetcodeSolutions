"""
Problem 1439: Find the Kth Smallest Sum of a Matrix With Sorted Rows
==================================================================
Difficulty: Hard
Tags: Array, Binary Search, Heap (Priority Queue), Matrix
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not mat:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in mat:
            heapq.heappush(heap, val)
            if len(heap) > (k if isinstance(k, int) else len(mat)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
