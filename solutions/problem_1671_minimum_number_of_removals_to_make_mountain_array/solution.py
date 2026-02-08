"""
Problem 1671: Minimum Number of Removals to Make Mountain Array
=============================================================
Difficulty: Hard
Tags: Array, Binary Search, Dynamic Programming, Greedy
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == nums:
                return mid
            elif nums[mid] < nums:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
