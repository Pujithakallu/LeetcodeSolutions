"""
Problem 1639: Number of Ways to Form a Target String Given a Dictionary
=====================================================================
Difficulty: Hard
Tags: Array, String, Dynamic Programming
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # String DP - O(m*n) time and space
        m, n = len(words), len(target)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if words[i-1] == target[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
