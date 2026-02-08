"""
Problem 749: Contain Virus
=========================
Difficulty: Hard
Tags: Array, Depth-First Search, Breadth-First Search, Matrix, Simulation
Pattern: DFS on Matrix / Grid

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        # DFS on grid - O(m*n) time
        if not isInfected:
            return 0
        rows, cols = len(isInfected), len(isInfected[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if isInfected[r][c] == '0' or isInfected[r][c] == 0:
                return
            isInfected[r][c] = '0'
            dfs(r+1, c); dfs(r-1, c)
            dfs(r, c+1); dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if isInfected[r][c] == '1' or isInfected[r][c] == 1:
                    dfs(r, c)
                    count += 1
        return count
