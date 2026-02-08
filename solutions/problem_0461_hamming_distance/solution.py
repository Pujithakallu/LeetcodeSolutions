"""
Problem 461: Hamming Distance
============================
Difficulty: Easy
Tags: Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in x:
            result ^= val
        return result
