"""
Problem 1401: Circle and Rectangle Overlapping
============================================
Difficulty: Medium
Tags: Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Geometry approach
        import math
        result = 0
        for i in range(len(radius)):
            for j in range(i + 1, len(radius)):
                dx = radius[i][0] - radius[j][0]
                dy = radius[i][1] - radius[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
