"""
Problem 649: Dota2 Senate
========================
Difficulty: Medium
Tags: String, Greedy, Queue
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(senate)):
            if isinstance(senate[i], int):
                curr_max = max(curr_max, senate[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
