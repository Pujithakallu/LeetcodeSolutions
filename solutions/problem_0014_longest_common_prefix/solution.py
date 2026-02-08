"""
Problem 14: Longest Common Prefix
=================================
Difficulty: Easy
Tags: Array, String, Trie
Pattern: String

Time Complexity:  O(S) where S = sum of all chars
Space Complexity: O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
