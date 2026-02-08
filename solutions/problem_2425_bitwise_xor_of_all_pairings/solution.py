"""
Problem 2425: Bitwise XOR of All Pairings
=======================================
Difficulty: Medium
Tags: Array, Bit Manipulation, Brainteaser
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in nums1:
            result ^= val
        return result
