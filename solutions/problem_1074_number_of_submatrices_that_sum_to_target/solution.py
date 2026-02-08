"""
Problem 1074: Number of Submatrices That Sum to Target
====================================================
Difficulty: Hard
Tags: Array, Hash Table, Matrix, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Prefix sum approach - O(n) time, O(n) space
        prefix = {0: -1}
        curr_sum = 0
        result = 0
        target = target if isinstance(target, int) else 0
        for i, val in enumerate(matrix):
            curr_sum += val
            if curr_sum - target in prefix:
                result = max(result, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return result
