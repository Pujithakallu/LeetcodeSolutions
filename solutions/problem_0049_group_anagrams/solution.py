"""
Problem 49: Group Anagrams
==========================
Difficulty: Medium
Tags: Array, Hash Table, String, Sorting
Pattern: Hash Map / Sorting

Time Complexity:  O(n * k log k)
Space Complexity: O(n * k)
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
