"""
Problem 2448: Minimum Cost to Make Array Equal
============================================
Difficulty: Hard
Tags: Array, Binary Search, Greedy, Sorting, Prefix Sum
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == cost:
                return mid
            elif nums[mid] < cost:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
