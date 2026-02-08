"""
Problem 238: Product of Array Except Self
========================================
Difficulty: Medium
Tags: Array, Prefix Sum
Pattern: Prefix/Suffix Products

Time Complexity:  O(n)
Space Complexity: O(1) extra
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result
