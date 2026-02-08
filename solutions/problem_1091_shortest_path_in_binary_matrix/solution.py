"""
Problem 1091: Shortest Path in Binary Matrix
==========================================
Difficulty: Medium
Tags: Array, Breadth-First Search, Matrix
Pattern: BFS / Shortest Path

Time Complexity:  O(n^2)
Space Complexity: O(n^2)
"""

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        while queue:
            r, c, d = queue.popleft()
            if r == n-1 and c == n-1:
                return d
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc, d+1))
        return -1
