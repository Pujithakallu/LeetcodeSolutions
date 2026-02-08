"""
Problem 2468: Split Message Based on Limit
========================================
Difficulty: Hard
Tags: String, Binary Search, Enumeration
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(message) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if message[mid] == limit:
                return mid
            elif message[mid] < limit:
                lo = mid + 1
            else:
                hi = mid - 1
        return []
