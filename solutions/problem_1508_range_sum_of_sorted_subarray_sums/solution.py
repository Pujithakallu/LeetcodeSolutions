"""
Problem 1508: Range Sum of Sorted Subarray Sums
=============================================
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Sorting, Prefix Sum
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == n:
                return mid
            elif nums[mid] < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
