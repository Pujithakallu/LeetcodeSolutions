"""
Problem 491: Non-decreasing Subsequences
=======================================
Difficulty: Medium
Tags: Array, Hash Table, Backtracking, Bit Manipulation
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
