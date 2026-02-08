"""
Problem 1771: Maximize Palindrome Length From Subsequences
========================================================
Difficulty: Hard
Tags: String, Dynamic Programming
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        # String DP - O(m*n) time and space
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
