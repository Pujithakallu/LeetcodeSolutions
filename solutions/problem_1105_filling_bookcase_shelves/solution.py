"""
Problem 1105: Filling Bookcase Shelves
====================================
Difficulty: Medium
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (1D)

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not books:
            return 0
        n = len(books) if isinstance(books, list) else books
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
