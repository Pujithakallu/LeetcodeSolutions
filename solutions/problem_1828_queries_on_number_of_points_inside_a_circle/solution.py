"""
Problem 1828: Queries on Number of Points Inside a Circle
=======================================================
Difficulty: Medium
Tags: Array, Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
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
