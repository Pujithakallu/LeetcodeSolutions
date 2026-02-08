"""
Problem 1368: Minimum Cost to Make at Least One Valid Path in a Grid
==================================================================
Difficulty: Hard
Tags: Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
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
