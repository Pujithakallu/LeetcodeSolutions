"""
Problem 957: Prison Cells After N Days
=====================================
Difficulty: Medium
Tags: Array, Hash Table, Math, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in cells:
            result ^= val
        return result
