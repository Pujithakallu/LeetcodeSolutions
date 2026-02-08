"""
Problem 304: Range Sum Query 2D - Immutable
==========================================
Difficulty: Medium
Tags: Array, Design, Matrix, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # Initialize data structure
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return 0

