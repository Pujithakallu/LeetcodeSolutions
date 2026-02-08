"""
Problem 1987: Number of Unique Good Subsequences
==============================================
Difficulty: Hard
Tags: String, Dynamic Programming
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        # String DP - O(m*n) time and space
        m, n = len(binary), len(binary)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if binary[i-1] == binary[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
