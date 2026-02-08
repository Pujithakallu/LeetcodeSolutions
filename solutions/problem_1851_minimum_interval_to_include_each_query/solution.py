"""
Problem 1851: Minimum Interval to Include Each Query
==================================================
Difficulty: Hard
Tags: Array, Binary Search, Sweep Line, Sorting, Heap (Priority Queue)
Pattern: Heap + Sorting

Time Complexity:  O((n+q) log n)
Space Complexity: O(n+q)
"""

import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        sorted_q = sorted(enumerate(queries), key=lambda x: x[1])
        result = [-1] * len(queries)
        heap = []
        i = 0
        for qi, q in sorted_q:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                result[qi] = heap[0][0]
        return result
