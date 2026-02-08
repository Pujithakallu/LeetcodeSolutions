"""
Problem 517: Super Washing Machines
==================================
Difficulty: Hard
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(machines)):
            if isinstance(machines[i], int):
                curr_max = max(curr_max, machines[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
