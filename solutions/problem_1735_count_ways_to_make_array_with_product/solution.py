"""
Problem 1735: Count Ways to Make Array With Product
=================================================
Difficulty: Hard
Tags: Array, Math, Dynamic Programming, Combinatorics, Number Theory
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not queries:
            return 0
        n = len(queries) if isinstance(queries, list) else queries
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
