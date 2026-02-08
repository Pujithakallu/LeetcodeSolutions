"""
Problem 223: Rectangle Area
==========================
Difficulty: Medium
Tags: Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Geometry approach
        import math
        result = 0
        for i in range(len(ax1)):
            for j in range(i + 1, len(ax1)):
                dx = ax1[i][0] - ax1[j][0]
                dy = ax1[i][1] - ax1[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
