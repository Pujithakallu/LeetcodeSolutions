"""
Problem 2397: Maximum Rows Covered by Columns
===========================================
Difficulty: Medium
Tags: Array, Backtracking, Bit Manipulation, Matrix, Enumeration
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(matrix)):
                path.append(matrix[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
