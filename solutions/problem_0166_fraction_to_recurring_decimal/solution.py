"""
Problem 166: Fraction to Recurring Decimal
=========================================
Difficulty: Medium
Tags: Hash Table, Math, String
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in numerator:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return numerator.index(ch)
        return ""
