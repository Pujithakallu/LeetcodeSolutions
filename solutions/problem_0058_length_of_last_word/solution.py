"""
Problem 58: Length of Last Word
===============================
Difficulty: Easy
Tags: String
Pattern: String

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split()[-1])
