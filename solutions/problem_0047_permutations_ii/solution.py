"""
Problem 47: Permutations II
===========================
Difficulty: Medium
Tags: Array, Backtracking, Sorting
Pattern: Backtracking

Time Complexity:  O(n!)
Space Complexity: O(n)
"""

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return result
