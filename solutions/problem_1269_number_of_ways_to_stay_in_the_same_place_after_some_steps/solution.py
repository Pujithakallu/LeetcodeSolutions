"""
Problem 1269: Number of Ways to Stay in the Same Place After Some Steps
=====================================================================
Difficulty: Hard
Tags: Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not steps:
            return 0
        n = len(steps) if isinstance(steps, list) else steps
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
