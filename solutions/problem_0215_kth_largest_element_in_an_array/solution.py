"""
Problem 215: Kth Largest Element in an Array
===========================================
Difficulty: Medium
Tags: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
Pattern: Heap / Quickselect

Time Complexity:  O(n log k)
Space Complexity: O(k)
"""

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
