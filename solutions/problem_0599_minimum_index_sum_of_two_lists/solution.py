"""
Problem 599: Minimum Index Sum of Two Lists
==========================================
Difficulty: Easy
Tags: Array, Hash Table, String
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(list1):
            complement = list2 - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []
