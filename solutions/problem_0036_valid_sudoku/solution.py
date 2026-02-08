"""
Problem 36: Valid Sudoku
========================
Difficulty: Medium
Tags: Array, Hash Table, Matrix
Pattern: Hash Set

Time Complexity:  O(1) (fixed 9x9 board)
Space Complexity: O(1)
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                box_idx = (i // 3) * 3 + j // 3
                if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
        return True
