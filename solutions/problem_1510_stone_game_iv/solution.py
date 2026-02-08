"""
Problem 1510: Stone Game IV
=========================
Difficulty: Hard
Tags: Math, Dynamic Programming, Game Theory
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not n:
            return 0
        n = len(n) if isinstance(n, list) else n
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
