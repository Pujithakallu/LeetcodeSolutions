"""
Problem 818: Race Car
====================
Difficulty: Hard
Tags: Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def racecar(self, target: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not target:
            return 0
        n = len(target) if isinstance(target, list) else target
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
