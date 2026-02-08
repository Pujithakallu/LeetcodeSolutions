"""
Problem 1720: Decode XORed Array
==============================
Difficulty: Easy
Tags: Array, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in encoded:
            result ^= val
        return result
