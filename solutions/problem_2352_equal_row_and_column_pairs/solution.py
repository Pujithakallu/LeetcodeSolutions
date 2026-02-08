"""
Problem 2352: Equal Row and Column Pairs
======================================
Difficulty: Medium
Tags: Array, Hash Table, Matrix, Simulation
Pattern: Hash Map / Matrix

Time Complexity:  O(n^2)
Space Complexity: O(n^2)
"""

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        from collections import Counter
        rows = Counter(tuple(row) for row in grid)
        count = 0
        n = len(grid)
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            count += rows[col]
        return count
