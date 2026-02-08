"""
Problem 1992: Find All Groups of Farmland
=======================================
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search, Matrix
Pattern: DFS on Matrix / Grid

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # DFS on grid - O(m*n) time
        if not land:
            return 0
        rows, cols = len(land), len(land[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if land[r][c] == '0' or land[r][c] == 0:
                return
            land[r][c] = '0'
            dfs(r+1, c); dfs(r-1, c)
            dfs(r, c+1); dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if land[r][c] == '1' or land[r][c] == 1:
                    dfs(r, c)
                    count += 1
        return count
