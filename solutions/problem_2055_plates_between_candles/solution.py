"""
Problem 2055: Plates Between Candles
==================================
Difficulty: Medium
Tags: Array, String, Binary Search, Prefix Sum
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(s) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if s[mid] == queries:
                return mid
            elif s[mid] < queries:
                lo = mid + 1
            else:
                hi = mid - 1
        return []
