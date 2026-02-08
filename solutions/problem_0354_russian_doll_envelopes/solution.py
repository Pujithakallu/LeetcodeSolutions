"""
Problem 354: Russian Doll Envelopes
==================================
Difficulty: Hard
Tags: Array, Binary Search, Dynamic Programming, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(envelopes) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if envelopes[mid] == envelopes:
                return mid
            elif envelopes[mid] < envelopes:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
