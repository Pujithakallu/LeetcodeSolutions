"""
Problem 698: Partition to K Equal Sum Subsets
============================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
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
