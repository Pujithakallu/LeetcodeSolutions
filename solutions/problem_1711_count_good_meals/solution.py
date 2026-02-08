"""
Problem 1711: Count Good Meals
============================
Difficulty: Medium
Tags: Array, Hash Table
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(deliciousness):
            complement = deliciousness - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
