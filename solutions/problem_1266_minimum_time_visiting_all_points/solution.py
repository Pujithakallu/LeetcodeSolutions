"""
Problem 1266: Minimum Time Visiting All Points
============================================
Difficulty: Easy
Tags: Array, Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # Geometry approach
        import math
        result = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
