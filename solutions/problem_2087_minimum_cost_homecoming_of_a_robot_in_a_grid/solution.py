"""
Problem 2087: Minimum Cost Homecoming of a Robot in a Grid
========================================================
Difficulty: Medium
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(startPos)):
            if isinstance(startPos[i], int):
                curr_max = max(curr_max, startPos[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
