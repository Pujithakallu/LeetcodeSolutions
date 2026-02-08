"""
Problem 2441: Largest Positive Integer That Exists With Its Negative
==================================================================
Difficulty: Easy
Tags: Array, Hash Table, Two Pointers, Sorting
Pattern: Two Pointers on Sorted Array

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # Sort + two pointers - O(n log n) time
        nums.sort()
        left, right = 0, len(nums) - 1
        result = 0
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < nums if isinstance(nums, int) else 0:
                left += 1
            else:
                right -= 1
        return result
