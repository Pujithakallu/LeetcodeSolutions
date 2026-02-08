"""
Problem 1342: Number of Steps to Reduce a Number to Zero
======================================================
Difficulty: Easy
Tags: Math, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in num:
            result ^= val
        return result
