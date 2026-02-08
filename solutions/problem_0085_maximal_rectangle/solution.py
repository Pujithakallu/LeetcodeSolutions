"""
Problem 85: Maximal Rectangle
=============================
Difficulty: Hard
Tags: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
Pattern: Monotonic Stack / DP

Time Complexity:  O(m*n)
Space Complexity: O(n)
"""

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            # Largest rectangle in histogram
            stack = []
            h = heights + [0]
            for i in range(len(h)):
                while stack and h[stack[-1]] > h[i]:
                    height = h[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
        return max_area
