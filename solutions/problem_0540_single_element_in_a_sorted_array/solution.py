"""
Problem 540: Single Element in a Sorted Array
============================================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]
