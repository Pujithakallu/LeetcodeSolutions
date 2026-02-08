"""
Problem 1713: Minimum Operations to Make a Subsequence
====================================================
Difficulty: Hard
Tags: Array, Hash Table, Binary Search, Greedy
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(target) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target[mid] == arr:
                return mid
            elif target[mid] < arr:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
