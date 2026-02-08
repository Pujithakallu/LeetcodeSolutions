"""
Problem 1139: Largest 1-Bordered Square
=====================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Matrix
Pattern: Dynamic Programming (2D Grid/Matrix)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # Dynamic programming (2D) - O(m*n) time and space
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                # Add problem-specific transition
        return dp[m][n]
