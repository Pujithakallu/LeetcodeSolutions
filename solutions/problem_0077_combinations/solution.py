"""
Problem 77: Combinations
========================
Difficulty: Medium
Tags: Backtracking
Pattern: Backtracking

Time Complexity:  O(C(n,k))
Space Complexity: O(k)
"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return result
