"""
Problem 1626: Best Team With No Conflicts
=======================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Sorting
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not scores:
            return 0
        n = len(scores) if isinstance(scores, list) else scores
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
