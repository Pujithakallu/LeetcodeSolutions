"""
Problem 781: Rabbits in Forest
=============================
Difficulty: Medium
Tags: Array, Hash Table, Math, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(answers)):
            if isinstance(answers[i], int):
                curr_max = max(curr_max, answers[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
