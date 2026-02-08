"""
Problem 27: Remove Element
==========================
Difficulty: Easy
Tags: Array, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write = 0
        for num in nums:
            if num != val:
                nums[write] = num
                write += 1
        return write
