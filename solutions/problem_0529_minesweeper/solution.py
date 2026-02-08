"""
Problem 529: Minesweeper
=======================
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search, Matrix
Pattern: DFS on Matrix / Grid

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # DFS on grid - O(m*n) time
        if not board:
            return 0
        rows, cols = len(board), len(board[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if board[r][c] == '0' or board[r][c] == 0:
                return
            board[r][c] = '0'
            dfs(r+1, c); dfs(r-1, c)
            dfs(r, c+1); dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '1' or board[r][c] == 1:
                    dfs(r, c)
                    count += 1
        return count
