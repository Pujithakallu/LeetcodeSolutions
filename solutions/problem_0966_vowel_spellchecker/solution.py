"""
Problem 966: Vowel Spellchecker
==============================
Difficulty: Medium
Tags: Array, Hash Table, String
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(wordlist):
            complement = queries - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []
