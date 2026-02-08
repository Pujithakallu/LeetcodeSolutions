"""
Problem 2033: Minimum Operations to Make a Uni-Value Grid
=======================================================
Difficulty: Medium
Tags: Array, Math, Sorting, Matrix
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Sort-based approach - O(n log n) time
        grid.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [grid[0]]
        for i in range(1, len(grid)):
            curr = grid[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
