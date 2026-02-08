"""
Problem 1418: Display Table of Food Orders in a Restaurant
========================================================
Difficulty: Medium
Tags: Array, Hash Table, String, Sorting, Ordered Set
Pattern: Ordered Set / SortedList

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # Ordered set / SortedList - O(n log n) time
        from sortedcontainers import SortedList
        sl = SortedList()
        result = 0
        for val in orders:
            pos = sl.bisect_left(val)
            if pos < len(sl):
                result = max(result, sl[pos] - val)
            sl.add(val)
        return result
