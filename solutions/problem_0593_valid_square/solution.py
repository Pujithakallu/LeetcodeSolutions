"""
Problem 593: Valid Square
========================
Difficulty: Medium
Tags: Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Geometry approach
        import math
        result = 0
        for i in range(len(p1)):
            for j in range(i + 1, len(p1)):
                dx = p1[i][0] - p1[j][0]
                dy = p1[i][1] - p1[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
