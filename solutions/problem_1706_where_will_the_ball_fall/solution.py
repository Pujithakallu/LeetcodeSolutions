"""
Problem 1706: Where Will the Ball Fall
====================================
Difficulty: Medium
Tags: Array, Matrix, Simulation
Pattern: Simulation

Time Complexity:  O(m*n)
Space Complexity: O(1) extra
"""

class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        result = []
        for col in range(n):
            c = col
            for r in range(m):
                d = grid[r][c]
                nc = c + d
                if nc < 0 or nc >= n or grid[r][nc] != d:
                    c = -1
                    break
                c = nc
            result.append(c)
        return result
