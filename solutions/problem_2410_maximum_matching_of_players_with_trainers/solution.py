"""
Problem 2410: Maximum Matching of Players With Trainers
=====================================================
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sort + greedy - O(n log n) time
        players.sort()
        result = 0
        curr_end = 0
        for item in players:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
