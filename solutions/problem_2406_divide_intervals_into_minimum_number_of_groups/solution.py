"""
Problem 2406: Divide Intervals Into Minimum Number of Groups
==========================================================
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not intervals:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in intervals:
            heapq.heappush(heap, val)
            if len(heap) > (intervals if isinstance(intervals, int) else len(intervals)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
