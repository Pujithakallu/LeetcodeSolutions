"""
Problem 1883: Minimum Skips to Arrive at Meeting On Time
======================================================
Difficulty: Hard
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not dist:
            return 0
        n = len(dist) if isinstance(dist, list) else dist
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
