"""
Problem 48: Rotate Image
========================
Difficulty: Medium
Tags: Array, Math, Matrix
Pattern: Matrix Manipulation

Time Complexity:  O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
