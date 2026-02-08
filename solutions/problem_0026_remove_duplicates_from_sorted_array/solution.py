"""
Problem 26: Remove Duplicates from Sorted Array
===============================================
Difficulty: Easy
Tags: Array, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        return write
