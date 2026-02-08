"""
Problem 1962: Remove Stones to Minimize the Total
===============================================
Difficulty: Medium
Tags: Array, Greedy, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not piles:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in piles:
            heapq.heappush(heap, val)
            if len(heap) > (k if isinstance(k, int) else len(piles)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
