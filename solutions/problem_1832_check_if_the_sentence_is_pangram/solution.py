"""
Problem 1832: Check if the Sentence Is Pangram
============================================
Difficulty: Easy
Tags: Hash Table, String
Pattern: Hash Map String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in sentence:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return sentence.index(ch)
        return False
