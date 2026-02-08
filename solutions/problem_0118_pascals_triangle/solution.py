"""
Problem 118: Pascal's Triangle
=============================
Difficulty: Easy
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not numRows:
            return 0
        n = len(numRows) if isinstance(numRows, list) else numRows
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
