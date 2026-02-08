"""
Problem 273: Integer to English Words
====================================
Difficulty: Hard
Tags: Math, String, Recursion
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        # Mathematical approach
        result = 0
        x = num
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
