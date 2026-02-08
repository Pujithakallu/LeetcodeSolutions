"""
Problem 875: Koko Eating Bananas
===============================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search on Answer

Time Complexity:  O(n log m)
Space Complexity: O(1)
"""

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            if hours <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo
