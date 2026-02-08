"""
Problem 1760: Minimum Limit of Balls in a Bag
===========================================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == maxOperations:
                return mid
            elif nums[mid] < maxOperations:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
