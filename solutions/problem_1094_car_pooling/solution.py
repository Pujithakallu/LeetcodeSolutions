"""
Problem 1094: Car Pooling
=======================
Difficulty: Medium
Tags: Array, Sorting, Heap (Priority Queue), Simulation, Prefix Sum
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not trips:
            return False
        # Min heap (negate for max heap)
        heap = []
        for val in trips:
            heapq.heappush(heap, val)
            if len(heap) > (capacity if isinstance(capacity, int) else len(trips)):
                heapq.heappop(heap)
        return heap[0] if heap else False
