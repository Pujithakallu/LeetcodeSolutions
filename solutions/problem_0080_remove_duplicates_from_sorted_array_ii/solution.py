"""
Problem 80: Remove Duplicates from Sorted Array II
==================================================
Difficulty: Medium
Tags: Array, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 0
        for num in nums:
            if write < 2 or num != nums[write - 2]:
                nums[write] = num
                write += 1
        return write
