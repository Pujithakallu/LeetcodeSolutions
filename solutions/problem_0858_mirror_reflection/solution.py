"""
Problem 858: Mirror Reflection
=============================
Difficulty: Medium
Tags: Math, Geometry, Number Theory
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Geometry approach
        import math
        result = 0
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                dx = p[i][0] - p[j][0]
                dy = p[i][1] - p[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
