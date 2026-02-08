"""
Problem 819: Most Common Word
============================
Difficulty: Easy
Tags: Array, Hash Table, String, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(paragraph):
            complement = banned - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return ""
