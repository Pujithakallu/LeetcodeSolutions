"""
Problem 822: Card Flipping Game
==============================
Difficulty: Medium
Tags: Array, Hash Table
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(fronts):
            complement = backs - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
