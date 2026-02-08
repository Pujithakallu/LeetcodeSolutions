"""
Problem 1657: Determine if Two Strings Are Close
==============================================
Difficulty: Medium
Tags: Hash Table, String, Sorting, Counting
Pattern: Hash Map / String

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        if len(word1) != len(word2):
            return False
        c1, c2 = Counter(word1), Counter(word2)
        return set(c1.keys()) == set(c2.keys()) and sorted(c1.values()) == sorted(c2.values())
