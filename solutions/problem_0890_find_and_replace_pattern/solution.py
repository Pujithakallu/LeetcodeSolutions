"""
Problem 890: Find and Replace Pattern
====================================
Difficulty: Medium
Tags: Array, Hash Table, String
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(words):
            complement = pattern - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []
