"""
Problem 1397: Find All Good Strings
=================================
Difficulty: Hard
Tags: String, Dynamic Programming, String Matching
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        # String DP - O(m*n) time and space
        m, n = len(n), len(s1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if n[i-1] == s1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
