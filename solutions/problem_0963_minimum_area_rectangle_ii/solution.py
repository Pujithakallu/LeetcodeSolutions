"""
Problem 963: Minimum Area Rectangle II
=====================================
Difficulty: Medium
Tags: Array, Hash Table, Math, Geometry
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(points):
            complement = points - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0.0
