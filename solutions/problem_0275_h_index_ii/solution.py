"""
Problem 275: H-Index II
======================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(citations) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if citations[mid] == citations:
                return mid
            elif citations[mid] < citations:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
