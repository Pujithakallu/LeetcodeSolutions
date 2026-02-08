"""
Problem 719: Find K-th Smallest Pair Distance
============================================
Difficulty: Hard
Tags: Array, Two Pointers, Binary Search, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == k:
                return mid
            elif nums[mid] < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
