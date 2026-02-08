"""
Problem 1805: Number of Different Integers in a String
====================================================
Difficulty: Easy
Tags: Hash Table, String
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return word.index(ch)
        return 0
