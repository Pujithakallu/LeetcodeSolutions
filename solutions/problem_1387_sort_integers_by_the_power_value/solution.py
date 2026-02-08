"""
Problem 1387: Sort Integers by The Power Value
============================================
Difficulty: Medium
Tags: Dynamic Programming, Memoization, Sorting
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not lo:
            return 0
        n = len(lo) if isinstance(lo, list) else lo
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
