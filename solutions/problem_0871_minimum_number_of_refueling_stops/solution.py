"""
Problem 871: Minimum Number of Refueling Stops
=============================================
Difficulty: Hard
Tags: Array, Dynamic Programming, Greedy, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not target:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in target:
            heapq.heappush(heap, val)
            if len(heap) > (startFuel if isinstance(startFuel, int) else len(target)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
