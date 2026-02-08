"""
Problem 1263: Minimum Moves to Move a Box to Their Target Location
================================================================
Difficulty: Hard
Tags: Array, Breadth-First Search, Heap (Priority Queue), Matrix
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
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
