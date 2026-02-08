"""
Problem 452: Minimum Number of Arrows to Burst Balloons
======================================================
Difficulty: Medium
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort + greedy - O(n log n) time
        points.sort()
        result = 0
        curr_end = 0
        for item in points:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
