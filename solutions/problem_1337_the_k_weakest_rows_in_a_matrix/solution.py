"""
Problem 1337: The K Weakest Rows in a Matrix
==========================================
Difficulty: Easy
Tags: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix
Pattern: Heap / Sorting

Time Complexity:  O(m*n + k*log m)
Space Complexity: O(m)
"""

import heapq

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        strengths = [(sum(row), i) for i, row in enumerate(mat)]
        heapq.heapify(strengths)
        return [heapq.heappop(strengths)[1] for _ in range(k)]
