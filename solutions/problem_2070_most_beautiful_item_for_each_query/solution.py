"""
Problem 2070: Most Beautiful Item for Each Query
==============================================
Difficulty: Medium
Tags: Array, Binary Search, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(items) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if items[mid] == queries:
                return mid
            elif items[mid] < queries:
                lo = mid + 1
            else:
                hi = mid - 1
        return []
