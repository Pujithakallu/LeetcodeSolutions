"""
Problem 1162: As Far from Land as Possible
========================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Breadth-First Search, Matrix
Pattern: Multi-source BFS

Time Complexity:  O(n^2)
Space Complexity: O(n^2)
"""

from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        dist = -1
        while queue:
            dist += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))
        return dist
