"""
Problem 1835: Find XOR Sum of All Pairs Bitwise AND
=================================================
Difficulty: Hard
Tags: Array, Math, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in arr1:
            result ^= val
        return result
