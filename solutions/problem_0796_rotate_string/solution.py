"""
Problem 796: Rotate String
=========================
Difficulty: Easy
Tags: String, String Matching
Pattern: String Matching

Time Complexity:  O(n + m)
Space Complexity: O(m)
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # String matching (KMP/Rolling Hash) - O(n+m) time
        if not goal or not s:
            return False
        n, m = len(s), len(goal)
        # Build failure function for KMP
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and goal[i] != goal[j]:
                j = fail[j-1]
            if goal[i] == goal[j]:
                j += 1
            fail[i] = j
        # Search
        j = 0
        for i in range(n):
            while j > 0 and s[i] != goal[j]:
                j = fail[j-1]
            if s[i] == goal[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1
