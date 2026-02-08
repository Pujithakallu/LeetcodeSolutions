"""
Problem 2038: Remove Colored Pieces if Both Neighbors are the Same Color
======================================================================
Difficulty: Medium
Tags: Math, String, Greedy, Game Theory
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(colors)):
            if isinstance(colors[i], int):
                curr_max = max(curr_max, colors[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
