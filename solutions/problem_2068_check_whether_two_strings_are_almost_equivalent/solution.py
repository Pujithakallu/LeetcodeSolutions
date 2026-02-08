"""
Problem 2068: Check Whether Two Strings are Almost Equivalent
===========================================================
Difficulty: Easy
Tags: Hash Table, String, Counting
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in word1:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return word1.index(ch)
        return False
