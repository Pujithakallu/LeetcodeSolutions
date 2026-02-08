"""
Problem 1897: Redistribute Characters to Make All Strings Equal
=============================================================
Difficulty: Easy
Tags: Hash Table, String, Counting
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in words:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return words.index(ch)
        return False
