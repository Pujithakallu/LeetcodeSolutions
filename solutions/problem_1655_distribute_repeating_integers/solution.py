"""
Problem 1655: Distribute Repeating Integers
=========================================
Difficulty: Hard
Tags: Array, Hash Table, Dynamic Programming, Backtracking, Bit Manipulation, Counting, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
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
