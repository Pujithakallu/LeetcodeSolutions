"""
Problem 121: Best Time to Buy and Sell Stock
===========================================
Difficulty: Easy
Tags: Array, Dynamic Programming
Pattern: Greedy / One Pass

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
