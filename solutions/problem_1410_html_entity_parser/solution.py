"""
Problem 1410: HTML Entity Parser
==============================
Difficulty: Medium
Tags: Hash Table, String
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def entityParser(self, text: str) -> str:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return text.index(ch)
        return ""
