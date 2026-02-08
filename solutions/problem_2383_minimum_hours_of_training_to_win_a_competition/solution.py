"""
Problem 2383: Minimum Hours of Training to Win a Competition
==========================================================
Difficulty: Easy
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(initialEnergy)):
            if isinstance(initialEnergy[i], int):
                curr_max = max(curr_max, initialEnergy[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
