"""
Problem 1452: People Whose List of Favorite Companies Is Not a Subset of Another List
===================================================================================
Difficulty: Medium
Tags: Array, Hash Table, String
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(favoriteCompanies):
            complement = favoriteCompanies - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []
