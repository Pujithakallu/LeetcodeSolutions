"""
Problem 391: Perfect Rectangle
=============================
Difficulty: Hard
Tags: Array, Hash Table, Math, Geometry, Sweep Line
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(rectangles):
            complement = rectangles - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return False
