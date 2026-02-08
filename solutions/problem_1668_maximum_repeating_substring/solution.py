"""
Problem 1668: Maximum Repeating Substring
=======================================
Difficulty: Easy
Tags: String, Dynamic Programming, String Matching
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # String DP - O(m*n) time and space
        m, n = len(sequence), len(word)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if sequence[i-1] == word[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
