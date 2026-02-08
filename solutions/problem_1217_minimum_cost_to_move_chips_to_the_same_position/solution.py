"""
Problem 1217: Minimum Cost to Move Chips to The Same Position
===========================================================
Difficulty: Easy
Tags: Array, Math, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(position)):
            if isinstance(position[i], int):
                curr_max = max(curr_max, position[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
