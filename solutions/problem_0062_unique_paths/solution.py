"""
Problem 62: Unique Paths
========================
Difficulty: Medium
Tags: Math, Dynamic Programming, Combinatorics
Pattern: Dynamic Programming

Time Complexity:  O(m*n)
Space Complexity: O(n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]
