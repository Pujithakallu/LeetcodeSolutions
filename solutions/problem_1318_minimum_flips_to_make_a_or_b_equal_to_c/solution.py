"""
Problem 1318: Minimum Flips to Make a OR b Equal to c
===================================================
Difficulty: Medium
Tags: Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in a:
            result ^= val
        return result
