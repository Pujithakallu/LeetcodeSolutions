"""
Problem 1335: Minimum Difficulty of a Job Schedule
================================================
Difficulty: Hard
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not jobDifficulty:
            return 0
        n = len(jobDifficulty) if isinstance(jobDifficulty, list) else jobDifficulty
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
