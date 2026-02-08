"""
Problem 37: Sudoku Solver
=========================
Difficulty: Hard
Tags: Array, Hash Table, Backtracking, Matrix
Pattern: Backtracking

Time Complexity:  O(9^(empty cells))
Space Complexity: O(81)
"""

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
                r, c = 3 * (row // 3) + i // 3, 3 * (col // 3) + i % 3
                if board[r][c] == num:
                    return False
            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(i, j, num):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve()
