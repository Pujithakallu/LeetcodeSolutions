"""
Problem 1392: Longest Happy Prefix
================================
Difficulty: Hard
Tags: String, Rolling Hash, String Matching, Hash Function
Pattern: String Matching

Time Complexity:  O(n + m)
Space Complexity: O(m)
"""

class Solution:
    def longestPrefix(self, s: str) -> str:
        # String matching (KMP/Rolling Hash) - O(n+m) time
        if not s or not s:
            return ""
        n, m = len(s), len(s)
        # Build failure function for KMP
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and s[i] != s[j]:
                j = fail[j-1]
            if s[i] == s[j]:
                j += 1
            fail[i] = j
        # Search
        j = 0
        for i in range(n):
            while j > 0 and s[i] != s[j]:
                j = fail[j-1]
            if s[i] == s[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1
