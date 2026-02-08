"""
Problem 53: Maximum Subarray
============================
Difficulty: Medium
Tags: Array, Divide and Conquer, Dynamic Programming
Pattern: Kadane's Algorithm (DP)

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
