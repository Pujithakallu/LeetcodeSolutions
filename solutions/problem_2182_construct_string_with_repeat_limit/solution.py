"""
Problem 2182: Construct String With Repeat Limit
==============================================
Difficulty: Medium
Tags: Hash Table, String, Greedy, Heap (Priority Queue), Counting
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not s:
            return ""
        # Min heap (negate for max heap)
        heap = []
        for val in s:
            heapq.heappush(heap, val)
            if len(heap) > (repeatLimit if isinstance(repeatLimit, int) else len(s)):
                heapq.heappop(heap)
        return heap[0] if heap else ""
