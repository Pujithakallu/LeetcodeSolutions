"""
Problem 1072: Flip Columns For Maximum Number of Equal Rows
=========================================================
Difficulty: Medium
Tags: Array, Hash Table, Matrix
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(matrix):
            complement = matrix - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
