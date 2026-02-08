"""
Problem 2209: Minimum White Tiles After Covering With Carpets
===========================================================
Difficulty: Hard
Tags: String, Dynamic Programming, Prefix Sum
Pattern: Dynamic Programming (String)

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        # String DP - O(m*n) time and space
        m, n = len(floor), len(numCarpets)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if floor[i-1] == numCarpets[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
