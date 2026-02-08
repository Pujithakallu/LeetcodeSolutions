"""
Problem 2234: Maximum Total Beauty of the Gardens
===============================================
Difficulty: Hard
Tags: Array, Two Pointers, Binary Search, Greedy, Sorting, Enumeration, Prefix Sum
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(flowers) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if flowers[mid] == newFlowers:
                return mid
            elif flowers[mid] < newFlowers:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
