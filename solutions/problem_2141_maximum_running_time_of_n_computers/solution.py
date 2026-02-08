"""
Problem 2141: Maximum Running Time of N Computers
===============================================
Difficulty: Hard
Tags: Array, Binary Search, Greedy, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(n) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if n[mid] == batteries:
                return mid
            elif n[mid] < batteries:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
