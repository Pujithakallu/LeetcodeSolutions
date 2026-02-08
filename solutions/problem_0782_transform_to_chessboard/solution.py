"""
Problem 782: Transform to Chessboard
===================================
Difficulty: Hard
Tags: Array, Math, Bit Manipulation, Matrix
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in board:
            result ^= val
        return result
