"""
Problem 63: Unique Paths II
===========================
Difficulty: Medium
Tags: Array, Dynamic Programming, Matrix
Pattern: Dynamic Programming

Time Complexity:  O(m*n)
Space Complexity: O(n)
"""

class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        dp = [0] * n
        dp[0] = 1
        for row in grid:
            for j in range(n):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[-1]
