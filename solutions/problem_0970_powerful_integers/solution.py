"""
Problem 970: Powerful Integers
=============================
Difficulty: Medium
Tags: Hash Table, Math, Enumeration
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(x):
            complement = y - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []
