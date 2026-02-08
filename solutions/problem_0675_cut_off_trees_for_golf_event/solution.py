"""
Problem 675: Cut Off Trees for Golf Event
========================================
Difficulty: Hard
Tags: Array, Breadth-First Search, Heap (Priority Queue), Matrix
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not forest:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in forest:
            heapq.heappush(heap, val)
            if len(heap) > (forest if isinstance(forest, int) else len(forest)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
