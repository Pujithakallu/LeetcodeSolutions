"""
Problem 28: Find the Index of the First Occurrence in a String
==============================================================
Difficulty: Easy
Tags: Two Pointers, String, String Matching
Pattern: String Matching

Time Complexity:  O(m*n)
Space Complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
