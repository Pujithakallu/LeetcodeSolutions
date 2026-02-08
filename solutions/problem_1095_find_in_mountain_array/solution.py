"""
Problem 1095: Find in Mountain Array
==================================
Difficulty: Hard
Tags: Array, Binary Search, Interactive
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(target) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target[mid] == mountainArr:
                return mid
            elif target[mid] < mountainArr:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
