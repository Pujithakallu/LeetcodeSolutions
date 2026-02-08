"""
Problem 1975: Maximum Matrix Sum
==============================
Difficulty: Medium
Tags: Array, Greedy, Matrix
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(matrix)):
            if isinstance(matrix[i], int):
                curr_max = max(curr_max, matrix[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
