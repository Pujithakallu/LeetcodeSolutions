"""
Problem 2056: Number of Valid Move Combinations On Chessboard
===========================================================
Difficulty: Hard
Tags: Array, String, Backtracking, Simulation
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(pieces)):
                path.append(pieces[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
