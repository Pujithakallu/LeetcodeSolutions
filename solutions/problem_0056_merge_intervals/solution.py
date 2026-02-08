"""
Problem 56: Merge Intervals
===========================
Difficulty: Medium
Tags: Array, Sorting
Pattern: Intervals / Sort

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged
