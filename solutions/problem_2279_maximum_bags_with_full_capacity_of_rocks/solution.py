"""
Problem 2279: Maximum Bags With Full Capacity of Rocks
====================================================
Difficulty: Medium
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # Sort + greedy - O(n log n) time
        capacity.sort()
        result = 0
        curr_end = 0
        for item in capacity:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
