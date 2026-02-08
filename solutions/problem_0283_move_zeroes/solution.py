"""
Problem 283: Move Zeroes
=======================
Difficulty: Easy
Tags: Array, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0
        for num in nums:
            if num != 0:
                nums[write] = num
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0
