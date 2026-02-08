"""
Problem 2466: Count Ways To Build Good Strings
============================================
Difficulty: Medium
Tags: Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not low:
            return 0
        n = len(low) if isinstance(low, list) else low
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
