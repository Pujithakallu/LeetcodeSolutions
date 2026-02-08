"""
Problem 762: Prime Number of Set Bits in Binary Representation
=============================================================
Difficulty: Easy
Tags: Math, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in left:
            result ^= val
        return result
