"""
Problem 546: Remove Boxes
========================
Difficulty: Hard
Tags: Array, Dynamic Programming, Memoization
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not boxes:
            return 0
        n = len(boxes) if isinstance(boxes, list) else boxes
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
