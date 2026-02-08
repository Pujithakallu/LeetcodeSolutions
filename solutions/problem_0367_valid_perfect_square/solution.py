"""
Problem 367: Valid Perfect Square
================================
Difficulty: Easy
Tags: Math, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(num) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if num[mid] == num:
                return mid
            elif num[mid] < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
