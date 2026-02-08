"""
Problem 914: X of a Kind in a Deck of Cards
==========================================
Difficulty: Easy
Tags: Array, Hash Table, Math, Counting, Number Theory
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(deck):
            complement = deck - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return False
