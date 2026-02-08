"""
Problem 2085: Count Common Words With One Occurrence
==================================================
Difficulty: Easy
Tags: Array, Hash Table, String, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(words1):
            complement = words2 - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
