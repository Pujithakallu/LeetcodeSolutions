"""
Problem 2235: Add Two Integers
============================
Difficulty: Easy
Tags: Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # Mathematical approach
        result = 0
        x = num1
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
