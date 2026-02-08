"""
Problem 2395: Find Subarrays With Equal Sum
=========================================
Difficulty: Easy
Tags: Array, Hash Table
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(nums):
            complement = nums - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return False
