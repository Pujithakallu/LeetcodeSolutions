"""
Problem 1356: Sort Integers by The Number of 1 Bits
=================================================
Difficulty: Easy
Tags: Array, Bit Manipulation, Sorting, Counting
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in arr:
            result ^= val
        return result
