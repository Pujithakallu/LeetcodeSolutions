"""
Problem 887: Super Egg Drop
==========================
Difficulty: Hard
Tags: Math, Binary Search, Dynamic Programming
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(k) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if k[mid] == n:
                return mid
            elif k[mid] < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
