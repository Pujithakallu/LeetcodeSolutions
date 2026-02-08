"""
Problem 128: Longest Consecutive Sequence
========================================
Difficulty: Medium
Tags: Array, Hash Table, Union-Find
Pattern: Hash Set

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
