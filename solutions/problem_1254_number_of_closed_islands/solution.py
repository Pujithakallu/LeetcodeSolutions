"""
Problem 1254: Number of Closed Islands
====================================
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
Pattern: DFS / Graph

Time Complexity:  O(m*n)
Space Complexity: O(m*n)
"""

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            a = dfs(r+1,c)
            b = dfs(r-1,c)
            c1 = dfs(r,c+1)
            d = dfs(r,c-1)
            return a and b and c1 and d
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and dfs(r, c):
                    count += 1
        return count
