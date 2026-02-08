"""
Problem 1138: Alphabet Board Path
===============================
Difficulty: Medium
Tags: Hash Table, String
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in target:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return target.index(ch)
        return ""
