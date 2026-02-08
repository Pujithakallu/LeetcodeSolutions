"""
Problem 2151: Maximum Good People Based on Statements
===================================================
Difficulty: Hard
Tags: Array, Backtracking, Bit Manipulation, Enumeration
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(statements)):
                path.append(statements[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
