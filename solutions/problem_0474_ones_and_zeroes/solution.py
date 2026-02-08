"""
Problem 474: Ones and Zeroes
===========================
Difficulty: Medium
Tags: Array, String, Dynamic Programming
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # String DP - O(m*n) time and space
        m, n = len(strs), len(m)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if strs[i-1] == m[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
