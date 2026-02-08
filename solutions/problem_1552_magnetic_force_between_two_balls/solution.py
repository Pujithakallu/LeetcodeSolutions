"""
Problem 1552: Magnetic Force Between Two Balls
============================================
Difficulty: Medium
Tags: Array, Binary Search, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(position) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if position[mid] == m:
                return mid
            elif position[mid] < m:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
