"""
Problem 168: Excel Sheet Column Title
====================================
Difficulty: Easy
Tags: Math, String
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Mathematical approach
        result = 0
        x = columnNumber
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
