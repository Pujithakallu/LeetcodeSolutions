"""
Problem 2498: Frog Jump II
========================
Difficulty: Medium
Tags: Array, Binary Search, Greedy
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(stones) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if stones[mid] == stones:
                return mid
            elif stones[mid] < stones:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
