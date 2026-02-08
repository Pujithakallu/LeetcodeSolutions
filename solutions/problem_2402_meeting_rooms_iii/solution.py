"""
Problem 2402: Meeting Rooms III
=============================
Difficulty: Hard
Tags: Array, Hash Table, Sorting, Heap (Priority Queue), Simulation
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not n:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in n:
            heapq.heappush(heap, val)
            if len(heap) > (meetings if isinstance(meetings, int) else len(n)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
