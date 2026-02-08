"""
Problem 240: Search a 2D Matrix II
=================================
Difficulty: Medium
Tags: Array, Binary Search, Divide and Conquer, Matrix
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid] == target:
                return mid
            elif matrix[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
