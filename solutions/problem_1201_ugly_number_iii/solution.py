"""
Problem 1201: Ugly Number III
===========================
Difficulty: Medium
Tags: Math, Binary Search, Combinatorics, Number Theory
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(n) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if n[mid] == a:
                return mid
            elif n[mid] < a:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
