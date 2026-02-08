"""
Problem 1923: Longest Common Subpath
==================================
Difficulty: Hard
Tags: Array, Binary Search, Rolling Hash, Suffix Array, Hash Function
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(n) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if n[mid] == paths:
                return mid
            elif n[mid] < paths:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
