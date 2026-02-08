"""
Problem 2332: The Latest Time to Catch a Bus
==========================================
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(buses) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if buses[mid] == passengers:
                return mid
            elif buses[mid] < passengers:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
