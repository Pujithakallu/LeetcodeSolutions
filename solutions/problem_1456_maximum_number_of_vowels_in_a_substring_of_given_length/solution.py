"""
Problem 1456: Maximum Number of Vowels in a Substring of Given Length
===================================================================
Difficulty: Medium
Tags: String, Sliding Window
Pattern: Sliding Window (Fixed)

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = sum(1 for c in s[:k] if c in vowels)
        max_count = count
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i-k] in vowels)
            max_count = max(max_count, count)
        return max_count
