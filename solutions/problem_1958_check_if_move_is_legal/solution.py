"""
Problem 1958: Check if Move is Legal
==================================
Difficulty: Medium
Tags: Array, Matrix, Enumeration
Pattern: Matrix / 2D Array

Time Complexity:  O(m * n)
Space Complexity: O(1) extra
"""

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        # Matrix manipulation - O(m*n) time
        if not board:
            return False
        m, n = len(board), len(board[0])
        # Process matrix in-place or build result
        for i in range(m):
            for j in range(n):
                pass  # Process board[i][j]
        return False
