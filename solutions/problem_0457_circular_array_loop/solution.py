"""
Problem 457: Circular Array Loop
===============================
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(nums) - 1
        while left < right:
            curr = nums[left] + nums[right]
            if curr == nums:
                return [left, right]
            elif curr < nums:
                left += 1
            else:
                right -= 1
        return False
