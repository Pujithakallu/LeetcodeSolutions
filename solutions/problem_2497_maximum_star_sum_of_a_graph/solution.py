"""
Problem 2497: Maximum Star Sum of a Graph
=======================================
Difficulty: Medium
Tags: Array, Greedy, Graph Theory, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not vals:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in vals:
            heapq.heappush(heap, val)
            if len(heap) > (edges if isinstance(edges, int) else len(vals)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
