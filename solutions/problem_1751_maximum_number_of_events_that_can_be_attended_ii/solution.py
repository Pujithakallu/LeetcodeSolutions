"""
Problem 1751: Maximum Number of Events That Can Be Attended II
============================================================
Difficulty: Hard
Tags: Array, Binary Search, Dynamic Programming, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(events) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if events[mid] == k:
                return mid
            elif events[mid] < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
