"""
Problem 1011: Capacity To Ship Packages Within D Days
===================================================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search on Answer

Time Complexity:  O(n log S)
Space Complexity: O(1)
"""

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            d, curr = 1, 0
            for w in weights:
                if curr + w > mid:
                    d += 1
                    curr = 0
                curr += w
            if d <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo
