"""
Problem 29: Divide Two Integers
===============================
Difficulty: Medium
Tags: Math, Bit Manipulation
Pattern: Bit Manipulation / Math

Time Complexity:  O(log^2 n)
Space Complexity: O(1)
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a, b = abs(dividend), abs(divisor)
        result = 0
        while a >= b:
            temp, multiple = b, 1
            while a >= temp << 1:
                temp <<= 1
                multiple <<= 1
            a -= temp
            result += multiple
        return sign * result
