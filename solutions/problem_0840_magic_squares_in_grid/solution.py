"""
Problem 840: Magic Squares In Grid
=================================
Difficulty: Medium
Tags: Array, Hash Table, Math, Matrix
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(grid):
            complement = grid - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
