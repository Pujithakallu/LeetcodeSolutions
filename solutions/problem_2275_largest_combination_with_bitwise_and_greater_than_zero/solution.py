"""
Problem 2275: Largest Combination With Bitwise AND Greater Than Zero
==================================================================
Difficulty: Medium
Tags: Array, Hash Table, Bit Manipulation, Counting
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in candidates:
            result ^= val
        return result
