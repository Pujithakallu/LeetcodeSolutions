"""
Problem 1406: Stone Game III
==========================
Difficulty: Hard
Tags: Array, Math, Dynamic Programming, Game Theory
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not stoneValue:
            return 0
        n = len(stoneValue) if isinstance(stoneValue, list) else stoneValue
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
