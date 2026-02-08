"""
Problem 518: Coin Change II
==========================
Difficulty: Medium
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming (Unbounded Knapsack)

Time Complexity:  O(n * amount)
Space Complexity: O(amount)
"""

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
