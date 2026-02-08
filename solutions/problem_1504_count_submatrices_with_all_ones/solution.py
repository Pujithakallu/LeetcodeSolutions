"""
Problem 1504: Count Submatrices With All Ones
===========================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # Monotonic stack - O(n) time, O(n) space
        n = len(mat)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and mat[i] > mat[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
