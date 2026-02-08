"""
Problem 393: UTF-8 Validation
============================
Difficulty: Medium
Tags: Array, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in data:
            result ^= val
        return result
