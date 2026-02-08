"""
Problem 2300: Successful Pairs of Spells and Potions
==================================================
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Sorting
Pattern: Binary Search + Sorting

Time Complexity:  O((m+n) log n)
Space Complexity: O(1) extra
"""

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        n = len(potions)
        result = []
        for spell in spells:
            needed = (success + spell - 1) // spell
            from bisect import bisect_left
            idx = bisect_left(potions, needed)
            result.append(n - idx)
        return result
