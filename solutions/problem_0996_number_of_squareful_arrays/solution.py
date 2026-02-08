"""
Problem 996: Number of Squareful Arrays
======================================
Difficulty: Hard
Tags: Array, Hash Table, Math, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
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
