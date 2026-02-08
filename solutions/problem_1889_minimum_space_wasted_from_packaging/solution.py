"""
Problem 1889: Minimum Space Wasted From Packaging
===============================================
Difficulty: Hard
Tags: Array, Binary Search, Sorting, Prefix Sum
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(packages) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if packages[mid] == boxes:
                return mid
            elif packages[mid] < boxes:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
