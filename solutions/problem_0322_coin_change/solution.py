"""
Problem 322: Coin Change
=======================
Difficulty: Medium
Tags: Array, Dynamic Programming, Breadth-First Search
Pattern: Dynamic Programming

Time Complexity:  O(n * amount)
Space Complexity: O(amount)
"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
