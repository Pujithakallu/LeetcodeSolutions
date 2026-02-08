"""
Problem 1475: Final Prices With a Special Discount in a Shop
==========================================================
Difficulty: Easy
Tags: Array, Stack, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Monotonic stack - O(n) time, O(n) space
        n = len(prices)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and prices[i] > prices[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
