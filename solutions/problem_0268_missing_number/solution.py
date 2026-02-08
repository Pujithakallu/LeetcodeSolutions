"""
Problem 268: Missing Number
==========================
Difficulty: Easy
Tags: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
Pattern: Math / XOR

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
