"""
Problem 1292: Maximum Side Length of a Square with Sum Less than or Equal to Threshold
====================================================================================
Difficulty: Medium
Tags: Array, Binary Search, Matrix, Prefix Sum
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(mat) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mat[mid] == threshold:
                return mid
            elif mat[mid] < threshold:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
