"""
Problem 363: Max Sum of Rectangle No Larger Than K
=================================================
Difficulty: Hard
Tags: Array, Binary Search, Matrix, Prefix Sum, Ordered Set
Pattern: Ordered Set / SortedList

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # Ordered set / SortedList - O(n log n) time
        from sortedcontainers import SortedList
        sl = SortedList()
        result = 0
        for val in matrix:
            pos = sl.bisect_left(val)
            if pos < len(sl):
                result = max(result, sl[pos] - val)
            sl.add(val)
        return result
