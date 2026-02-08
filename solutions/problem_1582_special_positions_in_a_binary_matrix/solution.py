"""
Problem 1582: Special Positions in a Binary Matrix
================================================
Difficulty: Easy
Tags: Array, Matrix
Pattern: Matrix / 2D Array

Time Complexity:  O(m * n)
Space Complexity: O(1) extra
"""

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Matrix manipulation - O(m*n) time
        if not mat:
            return 0
        m, n = len(mat), len(mat[0])
        # Process matrix in-place or build result
        for i in range(m):
            for j in range(n):
                pass  # Process mat[i][j]
        return 0
