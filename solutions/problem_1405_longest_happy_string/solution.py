"""
Problem 1405: Longest Happy String
================================
Difficulty: Medium
Tags: String, Greedy, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not a:
            return ""
        # Min heap (negate for max heap)
        heap = []
        for val in a:
            heapq.heappush(heap, val)
            if len(heap) > (b if isinstance(b, int) else len(a)):
                heapq.heappop(heap)
        return heap[0] if heap else ""
