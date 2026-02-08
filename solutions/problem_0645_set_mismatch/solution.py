"""
Problem 645: Set Mismatch
========================
Difficulty: Easy
Tags: Array, Hash Table, Bit Manipulation, Sorting
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in nums:
            result ^= val
        return result
