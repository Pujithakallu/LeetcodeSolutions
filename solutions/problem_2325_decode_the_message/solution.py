"""
Problem 2325: Decode the Message
==============================
Difficulty: Easy
Tags: Hash Table, String
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in key:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return key.index(ch)
        return ""
