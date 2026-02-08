"""
Problem 2310: Sum of Numbers With Units Digit K
=============================================
Difficulty: Medium
Tags: Math, Dynamic Programming, Greedy, Enumeration
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not num:
            return 0
        n = len(num) if isinstance(num, list) else num
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
