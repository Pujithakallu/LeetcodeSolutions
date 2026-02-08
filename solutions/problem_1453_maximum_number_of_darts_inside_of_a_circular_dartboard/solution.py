"""
Problem 1453: Maximum Number of Darts Inside of a Circular Dartboard
==================================================================
Difficulty: Hard
Tags: Array, Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        # Geometry approach
        import math
        result = 0
        for i in range(len(darts)):
            for j in range(i + 1, len(darts)):
                dx = darts[i][0] - darts[j][0]
                dy = darts[i][1] - darts[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
