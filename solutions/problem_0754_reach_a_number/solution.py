"""
Problem 754: Reach a Number
==========================
Difficulty: Medium
Tags: Math, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def reachNumber(self, target: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(target) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target[mid] == target:
                return mid
            elif target[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
