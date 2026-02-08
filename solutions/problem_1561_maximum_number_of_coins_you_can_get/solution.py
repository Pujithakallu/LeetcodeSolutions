"""
Problem 1561: Maximum Number of Coins You Can Get
===============================================
Difficulty: Medium
Tags: Array, Math, Greedy, Sorting, Game Theory
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Sort + greedy - O(n log n) time
        piles.sort()
        result = 0
        curr_end = 0
        for item in piles:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
