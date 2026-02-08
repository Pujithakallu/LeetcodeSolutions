"""
Problem 2190: Most Frequent Number Following Key In an Array
==========================================================
Difficulty: Easy
Tags: Array, Hash Table, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(nums):
            complement = key - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
