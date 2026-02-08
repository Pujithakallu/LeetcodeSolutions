"""
Problem 475: Heaters
===================
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(houses) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if houses[mid] == heaters:
                return mid
            elif houses[mid] < heaters:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
