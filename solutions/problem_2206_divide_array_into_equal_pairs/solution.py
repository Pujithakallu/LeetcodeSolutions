"""
Problem 2206: Divide Array Into Equal Pairs
=========================================
Difficulty: Easy
Tags: Array, Hash Table, Bit Manipulation, Counting
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in nums:
            result ^= val
        return result
