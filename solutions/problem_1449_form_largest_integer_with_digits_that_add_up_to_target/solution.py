"""
Problem 1449: Form Largest Integer With Digits That Add up to Target
==================================================================
Difficulty: Hard
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not cost:
            return 0
        n = len(cost) if isinstance(cost, list) else cost
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
