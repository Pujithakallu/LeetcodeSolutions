"""
Problem 1727: Largest Submatrix With Rearrangements
=================================================
Difficulty: Medium
Tags: Array, Greedy, Sorting, Matrix
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # Sort + greedy - O(n log n) time
        matrix.sort()
        result = 0
        curr_end = 0
        for item in matrix:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
