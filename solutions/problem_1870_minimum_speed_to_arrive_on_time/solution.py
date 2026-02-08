"""
Problem 1870: Minimum Speed to Arrive on Time
===========================================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(dist) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if dist[mid] == hour:
                return mid
            elif dist[mid] < hour:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
