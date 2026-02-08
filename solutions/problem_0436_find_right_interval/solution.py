"""
Problem 436: Find Right Interval
===============================
Difficulty: Medium
Tags: Array, Binary Search, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(intervals) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if intervals[mid] == intervals:
                return mid
            elif intervals[mid] < intervals:
                lo = mid + 1
            else:
                hi = mid - 1
        return []
