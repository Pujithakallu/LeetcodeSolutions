"""
Problem 1232: Check If It Is a Straight Line
==========================================
Difficulty: Easy
Tags: Array, Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Geometry approach
        import math
        result = 0
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                dx = coordinates[i][0] - coordinates[j][0]
                dy = coordinates[i][1] - coordinates[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
