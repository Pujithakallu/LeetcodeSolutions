"""
Problem 587: Erect the Fence
===========================
Difficulty: Hard
Tags: Array, Math, Geometry
Pattern: Geometry

Time Complexity:  O(n^2) or O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Geometry approach
        import math
        result = 0
        for i in range(len(trees)):
            for j in range(i + 1, len(trees)):
                dx = trees[i][0] - trees[j][0]
                dy = trees[i][1] - trees[j][1]
                dist = math.sqrt(dx*dx + dy*dy)
                result = max(result, dist)
        return result
