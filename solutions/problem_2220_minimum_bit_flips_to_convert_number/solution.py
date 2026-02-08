"""
Problem 2220: Minimum Bit Flips to Convert Number
===============================================
Difficulty: Easy
Tags: Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in start:
            result ^= val
        return result
