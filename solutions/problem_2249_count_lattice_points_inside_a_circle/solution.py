"""
Problem 2249: Count Lattice Points Inside a Circle
================================================
Difficulty: Medium
Tags: Array, Hash Table, Math, Geometry, Enumeration
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(circles):
            complement = circles - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
