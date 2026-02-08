"""
Problem 1288: Remove Covered Intervals
====================================
Difficulty: Medium
Tags: Array, Sorting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort-based approach - O(n log n) time
        intervals.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
