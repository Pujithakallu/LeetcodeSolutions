"""
Problem 793: Preimage Size of Factorial Zeroes Function
======================================================
Difficulty: Hard
Tags: Math, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(k) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if k[mid] == k:
                return mid
            elif k[mid] < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
