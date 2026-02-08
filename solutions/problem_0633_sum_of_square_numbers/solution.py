"""
Problem 633: Sum of Square Numbers
=================================
Difficulty: Medium
Tags: Math, Two Pointers, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(c) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if c[mid] == c:
                return mid
            elif c[mid] < c:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
