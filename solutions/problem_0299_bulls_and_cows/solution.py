"""
Problem 299: Bulls and Cows
==========================
Difficulty: Medium
Tags: Hash Table, String, Counting
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in secret:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return secret.index(ch)
        return ""
