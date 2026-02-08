"""
Problem 46: Permutations
========================
Difficulty: Medium
Tags: Array, Backtracking
Pattern: Backtracking

Time Complexity:  O(n!)
Space Complexity: O(n)
"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])
                return
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i+1:])
                path.pop()
        backtrack([], nums)
        return result
