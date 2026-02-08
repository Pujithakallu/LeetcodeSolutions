"""
Problem 149: Max Points on a Line
================================
Difficulty: Hard
Tags: Array, Hash Table, Math, Geometry
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(points):
            complement = points - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
