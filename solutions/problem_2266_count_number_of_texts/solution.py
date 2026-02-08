"""
Problem 2266: Count Number of Texts
=================================
Difficulty: Medium
Tags: Hash Table, Math, String, Dynamic Programming
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        # String DP - O(m*n) time and space
        m, n = len(pressedKeys), len(pressedKeys)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pressedKeys[i-1] == pressedKeys[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
