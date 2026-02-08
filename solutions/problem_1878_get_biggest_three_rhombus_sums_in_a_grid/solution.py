"""
Problem 1878: Get Biggest Three Rhombus Sums in a Grid
====================================================
Difficulty: Medium
Tags: Array, Math, Sorting, Heap (Priority Queue), Matrix, Prefix Sum
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not grid:
            return []
        # Min heap (negate for max heap)
        heap = []
        for val in grid:
            heapq.heappush(heap, val)
            if len(heap) > (grid if isinstance(grid, int) else len(grid)):
                heapq.heappop(heap)
        return heap[0] if heap else []
