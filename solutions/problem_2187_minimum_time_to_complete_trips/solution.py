"""
Problem 2187: Minimum Time to Complete Trips
==========================================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(time) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if time[mid] == totalTrips:
                return mid
            elif time[mid] < totalTrips:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
