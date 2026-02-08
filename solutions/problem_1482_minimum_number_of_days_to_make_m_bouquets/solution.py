"""
Problem 1482: Minimum Number of Days to Make m Bouquets
=====================================================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(bloomDay) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if bloomDay[mid] == m:
                return mid
            elif bloomDay[mid] < m:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
