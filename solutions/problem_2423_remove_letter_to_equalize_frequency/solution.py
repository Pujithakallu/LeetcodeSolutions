"""
Problem 2423: Remove Letter To Equalize Frequency
===============================================
Difficulty: Easy
Tags: Hash Table, String, Counting
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return word.index(ch)
        return False
