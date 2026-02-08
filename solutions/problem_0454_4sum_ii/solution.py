"""
Problem 454: 4Sum II
===================
Difficulty: Medium
Tags: Array, Hash Table
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(nums1):
            complement = nums2 - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
