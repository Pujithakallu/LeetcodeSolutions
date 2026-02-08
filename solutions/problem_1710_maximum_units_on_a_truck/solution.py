"""
Problem 1710: Maximum Units on a Truck
====================================
Difficulty: Easy
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort + greedy - O(n log n) time
        boxTypes.sort()
        result = 0
        curr_end = 0
        for item in boxTypes:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
