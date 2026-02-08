"""
Problem 22: Generate Parentheses
================================
Difficulty: Medium
Tags: String, Dynamic Programming, Backtracking
Pattern: Backtracking

Time Complexity:  O(4^n / sqrt(n))
Space Complexity: O(n)
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(path, open_count, close_count):
            if len(path) == 2 * n:
                result.append(''.join(path))
                return
            if open_count < n:
                path.append('(')
                backtrack(path, open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(')')
                backtrack(path, open_count, close_count + 1)
                path.pop()
        backtrack([], 0, 0)
        return result
