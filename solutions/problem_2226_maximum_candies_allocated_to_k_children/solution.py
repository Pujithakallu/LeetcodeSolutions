"""
Problem 2226: Maximum Candies Allocated to K Children
===================================================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(candies) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if candies[mid] == k:
                return mid
            elif candies[mid] < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
