"""
Problem 2272: Substring With Largest Variance
===========================================
Difficulty: Hard
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def largestVariance(self, s: str) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not s:
            return 0
        n = len(s) if isinstance(s, list) else s
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
