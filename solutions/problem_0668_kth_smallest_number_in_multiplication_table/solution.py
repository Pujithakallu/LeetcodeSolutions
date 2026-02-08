"""
Problem 668: Kth Smallest Number in Multiplication Table
=======================================================
Difficulty: Hard
Tags: Math, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(m) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if m[mid] == n:
                return mid
            elif m[mid] < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
