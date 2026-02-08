"""
Problem 2367: Number of Arithmetic Triplets
=========================================
Difficulty: Easy
Tags: Array, Hash Table, Two Pointers, Enumeration
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(nums) - 1
        while left < right:
            curr = nums[left] + nums[right]
            if curr == diff:
                return [left, right]
            elif curr < diff:
                left += 1
            else:
                right -= 1
        return 0
