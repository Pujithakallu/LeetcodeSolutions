"""
Problem 1981: Minimize the Difference Between Target and Chosen Elements
======================================================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Matrix
Pattern: Dynamic Programming (2D Grid/Matrix)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # Dynamic programming (2D) - O(m*n) time and space
        if not mat:
            return 0
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                # Add problem-specific transition
        return dp[m][n]
