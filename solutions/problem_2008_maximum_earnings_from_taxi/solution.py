"""
Problem 2008: Maximum Earnings From Taxi
======================================
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Dynamic Programming, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(n) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if n[mid] == rides:
                return mid
            elif n[mid] < rides:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
