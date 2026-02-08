"""
Problem 75: Sort Colors
=======================
Difficulty: Medium
Tags: Array, Two Pointers, Sorting
Pattern: Dutch National Flag / Three Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        lo, mid, hi = 0, 0, len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1; mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
