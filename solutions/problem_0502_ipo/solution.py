"""
Problem 502: IPO
===============
Difficulty: Hard
Tags: Array, Greedy, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not k:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in k:
            heapq.heappush(heap, val)
            if len(heap) > (w if isinstance(w, int) else len(k)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
