"""
Problem 916: Word Subsets
========================
Difficulty: Medium
Tags: Array, Hash Table, String
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(words1):
            complement = words2 - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []
