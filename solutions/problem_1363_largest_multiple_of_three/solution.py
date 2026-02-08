"""
Problem 1363: Largest Multiple of Three
=====================================
Difficulty: Hard
Tags: Array, Math, Dynamic Programming, Greedy, Sorting
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not digits:
            return 0
        n = len(digits) if isinstance(digits, list) else digits
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
