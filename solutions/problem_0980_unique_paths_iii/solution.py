"""
Problem 980: Unique Paths III
============================
Difficulty: Hard
Tags: Array, Backtracking, Bit Manipulation, Matrix
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(grid)):
                path.append(grid[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
