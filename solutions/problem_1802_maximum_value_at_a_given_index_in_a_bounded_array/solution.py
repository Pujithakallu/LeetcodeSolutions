"""
Problem 1802: Maximum Value at a Given Index in a Bounded Array
=============================================================
Difficulty: Medium
Tags: Math, Binary Search, Greedy
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(n) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if n[mid] == index:
                return mid
            elif n[mid] < index:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
