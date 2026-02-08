"""
Problem 1830: Minimum Number of Operations to Make String Sorted
==============================================================
Difficulty: Hard
Tags: Math, String, Combinatorics
Pattern: Combinatorics

Time Complexity:  O(n) or O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def makeStringSorted(self, s: str) -> int:
        # Combinatorics approach
        MOD = 10**9 + 7
        # Compute using factorials or DP
        n = s if isinstance(s, int) else len(s)
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i-1] * i % MOD
        return dp[n] % MOD
