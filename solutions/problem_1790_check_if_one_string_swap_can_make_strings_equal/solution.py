"""
Problem 1790: Check if One String Swap Can Make Strings Equal
===========================================================
Difficulty: Easy
Tags: Hash Table, String, Counting
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return s1.index(ch)
        return False
