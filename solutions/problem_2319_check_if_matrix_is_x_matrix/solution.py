"""
Problem 2319: Check if Matrix Is X-Matrix
=======================================
Difficulty: Easy
Tags: Array, Matrix
Pattern: Matrix / 2D Array

Time Complexity:  O(m * n)
Space Complexity: O(1) extra
"""

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        # Matrix manipulation - O(m*n) time
        if not grid:
            return False
        m, n = len(grid), len(grid[0])
        # Process matrix in-place or build result
        for i in range(m):
            for j in range(n):
                pass  # Process grid[i][j]
        return False
