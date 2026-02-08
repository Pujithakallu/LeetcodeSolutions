"""
Problem 198: House Robber
========================
Difficulty: Medium
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        prev2, prev1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
        return prev1
