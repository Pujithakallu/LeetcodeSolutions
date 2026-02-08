"""
Problem 2453: Destroy Sequential Targets
======================================
Difficulty: Medium
Tags: Array, Hash Table, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(nums):
            complement = space - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
