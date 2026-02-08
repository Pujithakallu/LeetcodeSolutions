"""
Problem 1404: Number of Steps to Reduce a Number in Binary Representation to One
==============================================================================
Difficulty: Medium
Tags: String, Bit Manipulation, Simulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def numSteps(self, s: str) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in s:
            result ^= val
        return result
