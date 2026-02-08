"""
Problem 810: Chalkboard XOR Game
===============================
Difficulty: Hard
Tags: Array, Math, Bit Manipulation, Brainteaser, Game Theory
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in nums:
            result ^= val
        return result
