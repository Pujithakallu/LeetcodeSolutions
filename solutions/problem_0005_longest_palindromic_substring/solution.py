"""
Problem 5: Longest Palindromic Substring
=========================================
Difficulty: Medium
Tags: Two Pointers, String, Dynamic Programming
Pattern: Expand Around Center

Time Complexity:  O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        result = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            result = max(result, odd, even, key=len)
        return result
