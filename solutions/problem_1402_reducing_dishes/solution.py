"""
Problem 1402: Reducing Dishes
===========================
Difficulty: Hard
Tags: Array, Dynamic Programming, Greedy, Sorting
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not satisfaction:
            return 0
        n = len(satisfaction) if isinstance(satisfaction, list) else satisfaction
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
