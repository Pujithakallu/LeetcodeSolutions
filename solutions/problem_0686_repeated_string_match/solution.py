"""
Problem 686: Repeated String Match
=================================
Difficulty: Medium
Tags: String, String Matching
Pattern: String Matching

Time Complexity:  O(n + m)
Space Complexity: O(m)
"""

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # String matching (KMP/Rolling Hash) - O(n+m) time
        if not b or not a:
            return 0
        n, m = len(a), len(b)
        # Build failure function for KMP
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and b[i] != b[j]:
                j = fail[j-1]
            if b[i] == b[j]:
                j += 1
            fail[i] = j
        # Search
        j = 0
        for i in range(n):
            while j > 0 and a[i] != b[j]:
                j = fail[j-1]
            if a[i] == b[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1
