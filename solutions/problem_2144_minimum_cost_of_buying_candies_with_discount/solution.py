"""
Problem 2144: Minimum Cost of Buying Candies With Discount
========================================================
Difficulty: Easy
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort + greedy - O(n log n) time
        cost.sort()
        result = 0
        curr_end = 0
        for item in cost:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
