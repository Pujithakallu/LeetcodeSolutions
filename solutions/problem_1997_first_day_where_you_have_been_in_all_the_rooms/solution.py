"""
Problem 1997: First Day Where You Have Been in All the Rooms
==========================================================
Difficulty: Medium
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not nextVisit:
            return 0
        n = len(nextVisit) if isinstance(nextVisit, list) else nextVisit
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
