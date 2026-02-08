"""
Problem 342: Power of Four
=========================
Difficulty: Easy
Tags: Math, Bit Manipulation, Recursion
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in n:
            result ^= val
        return result
