"""
Problem 2251: Number of Flowers in Full Bloom
===========================================
Difficulty: Hard
Tags: Array, Hash Table, Binary Search, Sorting, Prefix Sum, Ordered Set
Pattern: Ordered Set / SortedList

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Ordered set / SortedList - O(n log n) time
        from sortedcontainers import SortedList
        sl = SortedList()
        result = 0
        for val in flowers:
            pos = sl.bisect_left(val)
            if pos < len(sl):
                result = max(result, sl[pos] - val)
            sl.add(val)
        return result
