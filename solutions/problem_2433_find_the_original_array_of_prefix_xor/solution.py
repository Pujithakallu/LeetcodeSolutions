"""
Problem 2433: Find The Original Array of Prefix Xor
=================================================
Difficulty: Medium
Tags: Array, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in pref:
            result ^= val
        return result
