"""
Problem 1833: Maximum Ice Cream Bars
==================================
Difficulty: Medium
Tags: Array, Greedy, Sorting, Counting Sort
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Sort + greedy - O(n log n) time
        costs.sort()
        result = 0
        curr_end = 0
        for item in costs:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
