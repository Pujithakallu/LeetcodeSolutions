"""
Problem 1605: Find Valid Matrix Given Row and Column Sums
=======================================================
Difficulty: Medium
Tags: Array, Greedy, Matrix
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(rowSum)):
            if isinstance(rowSum[i], int):
                curr_max = max(curr_max, rowSum[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
