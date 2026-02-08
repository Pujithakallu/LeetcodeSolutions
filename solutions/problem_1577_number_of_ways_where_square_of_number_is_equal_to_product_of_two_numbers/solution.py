"""
Problem 1577: Number of Ways Where Square of Number Is Equal to Product of Two Numbers
====================================================================================
Difficulty: Medium
Tags: Array, Hash Table, Math, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(nums1) - 1
        while left < right:
            curr = nums1[left] + nums1[right]
            if curr == nums2:
                return [left, right]
            elif curr < nums2:
                left += 1
            else:
                right -= 1
        return 0
