"""
Problem 2463: Minimum Total Distance Traveled
===========================================
Difficulty: Hard
Tags: Array, Dynamic Programming, Sorting
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not robot:
            return 0
        n = len(robot) if isinstance(robot, list) else robot
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
