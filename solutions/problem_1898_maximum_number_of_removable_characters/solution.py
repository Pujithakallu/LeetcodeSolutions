"""
Problem 1898: Maximum Number of Removable Characters
==================================================
Difficulty: Medium
Tags: Array, Two Pointers, String, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(s) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if s[mid] == p:
                return mid
            elif s[mid] < p:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
