"""
Problem 2146: K Highest Ranked Items Within a Price Range
=======================================================
Difficulty: Medium
Tags: Array, Breadth-First Search, Sorting, Heap (Priority Queue), Matrix
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not grid:
            return []
        # Min heap (negate for max heap)
        heap = []
        for val in grid:
            heapq.heappush(heap, val)
            if len(heap) > (pricing if isinstance(pricing, int) else len(grid)):
                heapq.heappop(heap)
        return heap[0] if heap else []
