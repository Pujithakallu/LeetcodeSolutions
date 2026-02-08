"""
Problem 2285: Maximum Total Importance of Roads
=============================================
Difficulty: Medium
Tags: Greedy, Graph Theory, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not n:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in n:
            heapq.heappush(heap, val)
            if len(heap) > (roads if isinstance(roads, int) else len(n)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
