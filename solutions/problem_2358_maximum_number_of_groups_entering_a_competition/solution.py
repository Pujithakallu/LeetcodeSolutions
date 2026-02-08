"""
Problem 2358: Maximum Number of Groups Entering a Competition
===========================================================
Difficulty: Medium
Tags: Array, Math, Binary Search, Greedy
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(grades) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if grades[mid] == grades:
                return mid
            elif grades[mid] < grades:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
