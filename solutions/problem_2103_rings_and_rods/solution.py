"""
Problem 2103: Rings and Rods
==========================
Difficulty: Easy
Tags: Hash Table, String
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countPoints(self, rings: str) -> int:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in rings:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return rings.index(ch)
        return 0
