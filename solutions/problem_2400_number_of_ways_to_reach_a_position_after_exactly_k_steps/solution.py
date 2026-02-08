"""
Problem 2400: Number of Ways to Reach a Position After Exactly k Steps
====================================================================
Difficulty: Medium
Tags: Math, Dynamic Programming, Combinatorics
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not startPos:
            return 0
        n = len(startPos) if isinstance(startPos, list) else startPos
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
