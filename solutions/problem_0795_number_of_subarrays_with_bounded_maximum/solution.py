"""
Problem 795: Number of Subarrays with Bounded Maximum
====================================================
Difficulty: Medium
Tags: Array, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(nums) - 1
        while left < right:
            curr = nums[left] + nums[right]
            if curr == left:
                return [left, right]
            elif curr < left:
                left += 1
            else:
                right -= 1
        return 0
