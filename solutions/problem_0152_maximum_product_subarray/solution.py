"""
Problem 152: Maximum Product Subarray
====================================
Difficulty: Medium
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_prod = min_prod = result = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            result = max(result, max_prod)
        return result
