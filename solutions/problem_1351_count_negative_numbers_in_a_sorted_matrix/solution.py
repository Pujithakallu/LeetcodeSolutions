"""
Problem 1351: Count Negative Numbers in a Sorted Matrix
=====================================================
Difficulty: Easy
Tags: Array, Binary Search, Matrix
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(grid) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if grid[mid] == grid:
                return mid
            elif grid[mid] < grid:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
