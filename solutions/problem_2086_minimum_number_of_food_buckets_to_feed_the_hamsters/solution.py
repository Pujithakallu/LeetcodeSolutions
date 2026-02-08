"""
Problem 2086: Minimum Number of Food Buckets to Feed the Hamsters
===============================================================
Difficulty: Medium
Tags: String, Dynamic Programming, Greedy
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        # String DP - O(m*n) time and space
        m, n = len(hamsters), len(hamsters)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if hamsters[i-1] == hamsters[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
