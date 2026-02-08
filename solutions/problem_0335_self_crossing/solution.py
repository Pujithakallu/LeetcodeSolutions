"""
Problem 335: Self Crossing
=========================
Difficulty: Hard
Tags: Array, Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        # Geometry approach
        import math
        result = 0
        for i in range(len(distance)):
            for j in range(i + 1, len(distance)):
                dx = distance[i][0] - distance[j][0]
                dy = distance[i][1] - distance[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
