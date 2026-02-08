"""
Problem 2100: Find Good Days to Rob the Bank
==========================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Prefix Sum
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not security:
            return 0
        n = len(security) if isinstance(security, list) else security
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
