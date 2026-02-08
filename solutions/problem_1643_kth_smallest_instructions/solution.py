"""
Problem 1643: Kth Smallest Instructions
=====================================
Difficulty: Hard
Tags: Array, Math, Dynamic Programming, Combinatorics
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not destination:
            return 0
        n = len(destination) if isinstance(destination, list) else destination
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
