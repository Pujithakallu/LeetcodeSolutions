"""
Problem 902: Numbers At Most N Given Digit Set
=============================================
Difficulty: Hard
Tags: Array, Math, String, Binary Search, Dynamic Programming
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(digits) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if digits[mid] == n:
                return mid
            elif digits[mid] < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
