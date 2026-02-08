"""
Problem 78: Subsets
===================
Difficulty: Medium
Tags: Array, Backtracking, Bit Manipulation
Pattern: Backtracking

Time Complexity:  O(2^n)
Space Complexity: O(n)
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result
