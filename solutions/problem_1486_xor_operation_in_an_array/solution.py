"""
Problem 1486: XOR Operation in an Array
=====================================
Difficulty: Easy
Tags: Math, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in n:
            result ^= val
        return result
