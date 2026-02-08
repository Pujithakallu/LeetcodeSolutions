"""
Problem 1018: Binary Prefix Divisible By 5
========================================
Difficulty: Easy
Tags: Array, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in nums:
            result ^= val
        return result
