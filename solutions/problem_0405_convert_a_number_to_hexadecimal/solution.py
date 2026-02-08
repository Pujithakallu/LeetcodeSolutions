"""
Problem 405: Convert a Number to Hexadecimal
===========================================
Difficulty: Easy
Tags: Math, String, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def toHex(self, num: int) -> str:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in num:
            result ^= val
        return result
