"""
Problem 1048: Longest String Chain
================================
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, String, Dynamic Programming, Sorting
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # String DP - O(m*n) time and space
        m, n = len(words), len(words)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if words[i-1] == words[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
