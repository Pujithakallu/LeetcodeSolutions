"""
Problem 7: Reverse Integer
===========================
Difficulty: Medium
Tags: Math
Pattern: Math

Time Complexity:  O(log x)
Space Complexity: O(1)
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        result *= sign
        return result if -2**31 <= result <= 2**31 - 1 else 0
