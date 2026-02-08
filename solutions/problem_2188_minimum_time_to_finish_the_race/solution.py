"""
Problem 2188: Minimum Time to Finish the Race
===========================================
Difficulty: Hard
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not tires:
            return 0
        n = len(tires) if isinstance(tires, list) else tires
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
