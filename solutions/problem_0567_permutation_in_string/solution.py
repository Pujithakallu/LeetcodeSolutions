"""
Problem 567: Permutation in String
=================================
Difficulty: Medium
Tags: Hash Table, Two Pointers, String, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(1)
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])
        if window == s1_count:
            return True
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            left = s2[i - len(s1)]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == s1_count:
                return True
        return False
