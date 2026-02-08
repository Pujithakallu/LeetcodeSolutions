"""
Problem 51: N-Queens
====================
Difficulty: Hard
Tags: Array, Backtracking
Pattern: Backtracking

Time Complexity:  O(n!)
Space Complexity: O(n^2)
"""

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [['.' ] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
                cols.discard(col)
                diag1.discard(row - col)
                diag2.discard(row + col)
        backtrack(0)
        return result
