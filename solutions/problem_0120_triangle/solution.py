"""
Problem 120: Triangle
====================
Difficulty: Medium
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not triangle:
            return 0
        n = len(triangle) if isinstance(triangle, list) else triangle
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
