"""
Problem 2500: Delete Greatest Value in Each Row
=============================================
Difficulty: Easy
Tags: Array, Sorting, Heap (Priority Queue), Matrix, Simulation
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not grid:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in grid:
            heapq.heappush(heap, val)
            if len(heap) > (grid if isinstance(grid, int) else len(grid)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
