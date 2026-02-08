"""
Problem 76: Minimum Window Substring
====================================
Difficulty: Hard
Tags: Hash Table, String, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(m+n)
Space Complexity: O(m+n)
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        start, end = 0, float('inf')
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if right - left < end - start:
                    start, end = left, right
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return s[start:end+1] if end != float('inf') else '' 
