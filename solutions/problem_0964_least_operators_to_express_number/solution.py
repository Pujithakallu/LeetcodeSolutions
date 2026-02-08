"""
Problem 964: Least Operators to Express Number
=============================================
Difficulty: Hard
Tags: Math, Dynamic Programming, Memoization
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not x:
            return 0
        n = len(x) if isinstance(x, list) else x
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
