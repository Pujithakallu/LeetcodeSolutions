"""
Problem 1680: Concatenation of Consecutive Binary Numbers
=======================================================
Difficulty: Medium
Tags: Math, Bit Manipulation, Simulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in n:
            result ^= val
        return result
