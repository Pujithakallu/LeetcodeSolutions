"""
Problem 1408: String Matching in an Array
=======================================
Difficulty: Easy
Tags: Array, String, String Matching
Pattern: String Matching

Time Complexity:  O(n + m)
Space Complexity: O(m)
"""

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # String matching (KMP/Rolling Hash) - O(n+m) time
        if not words or not words:
            return []
        n, m = len(words), len(words)
        # Build failure function for KMP
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and words[i] != words[j]:
                j = fail[j-1]
            if words[i] == words[j]:
                j += 1
            fail[i] = j
        # Search
        j = 0
        for i in range(n):
            while j > 0 and words[i] != words[j]:
                j = fail[j-1]
            if words[i] == words[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1
