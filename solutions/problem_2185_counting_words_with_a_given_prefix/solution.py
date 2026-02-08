"""
Problem 2185: Counting Words With a Given Prefix
==============================================
Difficulty: Easy
Tags: Array, String, String Matching
Pattern: String Matching

Time Complexity:  O(n + m)
Space Complexity: O(m)
"""

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # String matching (KMP/Rolling Hash) - O(n+m) time
        if not pref or not words:
            return 0
        n, m = len(words), len(pref)
        # Build failure function for KMP
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pref[i] != pref[j]:
                j = fail[j-1]
            if pref[i] == pref[j]:
                j += 1
            fail[i] = j
        # Search
        j = 0
        for i in range(n):
            while j > 0 and words[i] != pref[j]:
                j = fail[j-1]
            if words[i] == pref[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1
