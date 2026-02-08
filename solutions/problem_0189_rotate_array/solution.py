"""
Problem 189: Rotate Array
========================
Difficulty: Medium
Tags: Array, Math, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(nums) - 1
        while left < right:
            curr = nums[left] + nums[right]
            if curr == k:
                return [left, right]
            elif curr < k:
                left += 1
            else:
                right -= 1
        return None
