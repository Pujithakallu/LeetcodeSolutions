"""
Problem 66: Plus One
====================
Difficulty: Easy
Tags: Array, Math
Pattern: Math / Array

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
