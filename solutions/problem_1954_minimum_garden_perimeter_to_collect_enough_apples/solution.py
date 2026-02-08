"""
Problem 1954: Minimum Garden Perimeter to Collect Enough Apples
=============================================================
Difficulty: Medium
Tags: Math, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(neededApples) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if neededApples[mid] == neededApples:
                return mid
            elif neededApples[mid] < neededApples:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
