"""
Problem 1606: Find Servers That Handled Most Number of Requests
=============================================================
Difficulty: Hard
Tags: Array, Heap (Priority Queue), Simulation, Ordered Set
Pattern: Ordered Set / SortedList

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Ordered set / SortedList - O(n log n) time
        from sortedcontainers import SortedList
        sl = SortedList()
        result = 0
        for val in k:
            pos = sl.bisect_left(val)
            if pos < len(sl):
                result = max(result, sl[pos] - val)
            sl.add(val)
        return result
