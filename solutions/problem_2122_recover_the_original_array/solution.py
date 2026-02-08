"""
Problem 2122: Recover the Original Array
======================================
Difficulty: Hard
Tags: Array, Hash Table, Two Pointers, Sorting, Enumeration
Pattern: Two Pointers on Sorted Array

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        # Sort + two pointers - O(n log n) time
        nums.sort()
        left, right = 0, len(nums) - 1
        result = []
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < nums if isinstance(nums, int) else 0:
                left += 1
            else:
                right -= 1
        return result
