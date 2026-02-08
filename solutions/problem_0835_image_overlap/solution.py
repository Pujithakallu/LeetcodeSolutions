"""
Problem 835: Image Overlap
=========================
Difficulty: Medium
Tags: Array, Matrix
Pattern: Matrix / 2D Array

Time Complexity:  O(m * n)
Space Complexity: O(1) extra
"""

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # Matrix manipulation - O(m*n) time
        if not img1:
            return 0
        m, n = len(img1), len(img1[0])
        # Process matrix in-place or build result
        for i in range(m):
            for j in range(n):
                pass  # Process img1[i][j]
        return 0
