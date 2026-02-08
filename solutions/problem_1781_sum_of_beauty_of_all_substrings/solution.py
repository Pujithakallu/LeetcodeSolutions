"""
Problem 1781: Sum of Beauty of All Substrings
===========================================
Difficulty: Medium
Tags: Hash Table, String, Counting
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def beautySum(self, s: str) -> int:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return s.index(ch)
        return 0
