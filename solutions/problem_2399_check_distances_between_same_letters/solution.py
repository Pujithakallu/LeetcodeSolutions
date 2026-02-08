"""
Problem 2399: Check Distances Between Same Letters
================================================
Difficulty: Easy
Tags: Array, Hash Table, String
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(s):
            complement = distance - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return False
