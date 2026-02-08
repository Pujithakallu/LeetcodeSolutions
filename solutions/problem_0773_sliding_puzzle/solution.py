"""
Problem 773: Sliding Puzzle
==========================
Difficulty: Hard
Tags: Array, Dynamic Programming, Backtracking, Breadth-First Search, Memoization, Matrix
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(board)):
                path.append(board[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
