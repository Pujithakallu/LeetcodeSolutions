"""
Problem 1901: Find a Peak Element II
==================================
Difficulty: Medium
Tags: Array, Binary Search, Matrix
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(mat) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mat[mid] == mat:
                return mid
            elif mat[mid] < mat:
                lo = mid + 1
            else:
                hi = mid - 1
        return []
