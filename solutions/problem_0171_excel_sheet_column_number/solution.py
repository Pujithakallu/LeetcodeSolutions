"""
Problem 171: Excel Sheet Column Number
=====================================
Difficulty: Easy
Tags: Math, String
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Mathematical approach
        result = 0
        x = columnTitle
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
