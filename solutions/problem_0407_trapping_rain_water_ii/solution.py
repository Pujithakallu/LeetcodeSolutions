"""
Problem 407: Trapping Rain Water II
==================================
Difficulty: Hard
Tags: Array, Breadth-First Search, Heap (Priority Queue), Matrix
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not heightMap:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in heightMap:
            heapq.heappush(heap, val)
            if len(heap) > (heightMap if isinstance(heightMap, int) else len(heightMap)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
