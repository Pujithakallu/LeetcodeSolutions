"""
Problem 1562: Find Latest Group of Size M
=======================================
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Simulation
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == m:
                return mid
            elif arr[mid] < m:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
