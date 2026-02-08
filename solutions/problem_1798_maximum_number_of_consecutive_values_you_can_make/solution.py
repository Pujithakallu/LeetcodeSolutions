"""
Problem 1798: Maximum Number of Consecutive Values You Can Make
=============================================================
Difficulty: Medium
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # Sort + greedy - O(n log n) time
        coins.sort()
        result = 0
        curr_end = 0
        for item in coins:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
