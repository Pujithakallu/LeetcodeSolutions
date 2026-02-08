"""
Problem 2419: Longest Subarray With Maximum Bitwise AND
=====================================================
Difficulty: Medium
Tags: Array, Bit Manipulation, Brainteaser
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in nums:
            result ^= val
        return result
