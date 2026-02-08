"""
Problem 771: Jewels and Stones
=============================
Difficulty: Easy
Tags: Hash Table, String
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in jewels:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return jewels.index(ch)
        return 0
