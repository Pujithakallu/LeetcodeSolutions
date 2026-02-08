"""
Problem 35: Search Insert Position
==================================
Difficulty: Easy
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
