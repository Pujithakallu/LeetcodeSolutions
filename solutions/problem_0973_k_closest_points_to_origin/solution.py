"""
Problem 973: K Closest Points to Origin
======================================
Difficulty: Medium
Tags: Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect
Pattern: Heap / Quickselect

Time Complexity:  O(n log k)
Space Complexity: O(k)
"""

import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            dist = -(x*x + y*y)
            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            elif dist > heap[0][0]:
                heapq.heapreplace(heap, (dist, x, y))
        return [[x, y] for _, x, y in heap]
