"""
Problem 2023: Number of Pairs of Strings With Concatenation Equal to Target
=========================================================================
Difficulty: Medium
Tags: Array, Hash Table, String, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
