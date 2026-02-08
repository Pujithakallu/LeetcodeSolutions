"""
Problem 2064: Minimized Maximum of Products Distributed to Any Store
==================================================================
Difficulty: Medium
Tags: Array, Binary Search, Greedy
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(n) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if n[mid] == quantities:
                return mid
            elif n[mid] < quantities:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
