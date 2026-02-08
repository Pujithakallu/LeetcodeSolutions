"""
Problem 90: Subsets II
======================
Difficulty: Medium
Tags: Array, Backtracking, Bit Manipulation
Pattern: Backtracking

Time Complexity:  O(2^n)
Space Complexity: O(n)
"""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result
