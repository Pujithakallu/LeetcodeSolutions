"""
Problem 609: Find Duplicate File in System
=========================================
Difficulty: Medium
Tags: Array, Hash Table, String
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(paths):
            complement = paths - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []
