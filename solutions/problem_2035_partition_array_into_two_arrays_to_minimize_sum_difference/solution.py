"""
Problem 2035: Partition Array Into Two Arrays to Minimize Sum Difference
======================================================================
Difficulty: Hard
Tags: Array, Two Pointers, Binary Search, Dynamic Programming, Bit Manipulation, Sorting, Ordered Set, Bitmask
Pattern: Ordered Set / SortedList

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # Ordered set / SortedList - O(n log n) time
        from sortedcontainers import SortedList
        sl = SortedList()
        result = 0
        for val in nums:
            pos = sl.bisect_left(val)
            if pos < len(sl):
                result = max(result, sl[pos] - val)
            sl.add(val)
        return result
