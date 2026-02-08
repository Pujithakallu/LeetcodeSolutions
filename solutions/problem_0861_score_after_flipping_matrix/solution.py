"""
Problem 861: Score After Flipping Matrix
=======================================
Difficulty: Medium
Tags: Array, Greedy, Bit Manipulation, Matrix
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(grid)):
            if isinstance(grid[i], int):
                curr_max = max(curr_max, grid[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
