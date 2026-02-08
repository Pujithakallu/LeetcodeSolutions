"""
Problem 136: Single Number
=========================
Difficulty: Easy
Tags: Array, Bit Manipulation
Pattern: Bit Manipulation (XOR)

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
