"""
Problem 724: Find Pivot Index
============================
Difficulty: Easy
Tags: Array, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        return -1
