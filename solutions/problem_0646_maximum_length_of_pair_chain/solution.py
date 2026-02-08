"""
Problem 646: Maximum Length of Pair Chain
========================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy, Sorting
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not pairs:
            return 0
        n = len(pairs) if isinstance(pairs, list) else pairs
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
