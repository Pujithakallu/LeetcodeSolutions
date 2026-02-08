"""
Problem 1370: Increasing Decreasing String
========================================
Difficulty: Easy
Tags: Hash Table, String, Counting
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def sortString(self, s: str) -> str:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return s.index(ch)
        return ""
