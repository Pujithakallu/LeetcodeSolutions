"""
Problem 1253: Reconstruct a 2-Row Binary Matrix
=============================================
Difficulty: Medium
Tags: Array, Greedy, Matrix
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(upper)):
            if isinstance(upper[i], int):
                curr_max = max(curr_max, upper[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
