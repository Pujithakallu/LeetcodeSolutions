"""
Problem 2481: Minimum Cuts to Divide a Circle
===========================================
Difficulty: Easy
Tags: Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def numberOfCuts(self, n: int) -> int:
        # Geometry approach
        import math
        result = 0
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                dx = n[i][0] - n[j][0]
                dy = n[i][1] - n[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
