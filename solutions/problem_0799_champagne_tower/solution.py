"""
Problem 799: Champagne Tower
===========================
Difficulty: Medium
Tags: Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not poured:
            return 0
        n = len(poured) if isinstance(poured, list) else poured
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
