"""
Problem 825: Friends Of Appropriate Ages
=======================================
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(ages) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if ages[mid] == ages:
                return mid
            elif ages[mid] < ages:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
