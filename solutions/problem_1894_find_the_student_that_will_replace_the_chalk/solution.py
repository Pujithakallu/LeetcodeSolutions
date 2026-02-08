"""
Problem 1894: Find the Student that Will Replace the Chalk
========================================================
Difficulty: Medium
Tags: Array, Binary Search, Simulation, Prefix Sum
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(chalk) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if chalk[mid] == k:
                return mid
            elif chalk[mid] < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
