"""
Problem 757: Set Intersection Size At Least Two
==============================================
Difficulty: Hard
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort + greedy - O(n log n) time
        intervals.sort()
        result = 0
        curr_end = 0
        for item in intervals:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
