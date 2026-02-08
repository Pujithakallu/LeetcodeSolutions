"""
Problem 1170: Compare Strings by Frequency of the Smallest Character
==================================================================
Difficulty: Medium
Tags: Array, Hash Table, String, Binary Search, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(queries) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if queries[mid] == words:
                return mid
            elif queries[mid] < words:
                lo = mid + 1
            else:
                hi = mid - 1
        return []
