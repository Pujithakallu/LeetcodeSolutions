"""
Problem 458: Poor Pigs
=====================
Difficulty: Hard
Tags: Math, Dynamic Programming, Combinatorics
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not buckets:
            return 0
        n = len(buckets) if isinstance(buckets, list) else buckets
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
