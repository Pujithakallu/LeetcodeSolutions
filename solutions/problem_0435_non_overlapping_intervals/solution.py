"""
Problem 435: Non-overlapping Intervals
=====================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy, Sorting
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not intervals:
            return 0
        n = len(intervals) if isinstance(intervals, list) else intervals
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
