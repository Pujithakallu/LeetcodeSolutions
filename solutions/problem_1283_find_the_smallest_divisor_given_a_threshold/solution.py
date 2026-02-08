"""
Problem 1283: Find the Smallest Divisor Given a Threshold
=======================================================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == threshold:
                return mid
            elif nums[mid] < threshold:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
