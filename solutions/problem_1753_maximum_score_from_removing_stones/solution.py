"""
Problem 1753: Maximum Score From Removing Stones
==============================================
Difficulty: Medium
Tags: Math, Greedy, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not a:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in a:
            heapq.heappush(heap, val)
            if len(heap) > (b if isinstance(b, int) else len(a)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
