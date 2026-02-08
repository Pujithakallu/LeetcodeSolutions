"""
Problem 553: Optimal Division
============================
Difficulty: Medium
Tags: Array, Math, Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not nums:
            return 0
        n = len(nums) if isinstance(nums, list) else nums
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
