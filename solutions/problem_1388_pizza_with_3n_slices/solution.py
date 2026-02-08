"""
Problem 1388: Pizza With 3n Slices
================================
Difficulty: Hard
Tags: Array, Dynamic Programming, Greedy, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not slices:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in slices:
            heapq.heappush(heap, val)
            if len(heap) > (slices if isinstance(slices, int) else len(slices)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
