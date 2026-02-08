"""
Problem 1931: Painting a Grid With Three Different Colors
=======================================================
Difficulty: Hard
Tags: Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not m:
            return 0
        n = len(m) if isinstance(m, list) else m
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
