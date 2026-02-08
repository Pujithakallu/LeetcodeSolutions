"""
Problem 416: Partition Equal Subset Sum
======================================
Difficulty: Medium
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (0/1 Knapsack)

Time Complexity:  O(n * sum/2)
Space Complexity: O(sum/2)
"""

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]
