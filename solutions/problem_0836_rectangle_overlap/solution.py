"""
Problem 836: Rectangle Overlap
=============================
Difficulty: Easy
Tags: Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Geometry approach
        import math
        result = 0
        for i in range(len(rec1)):
            for j in range(i + 1, len(rec1)):
                dx = rec1[i][0] - rec1[j][0]
                dy = rec1[i][1] - rec1[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
