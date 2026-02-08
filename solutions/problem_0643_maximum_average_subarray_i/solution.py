"""
Problem 643: Maximum Average Subarray I
======================================
Difficulty: Easy
Tags: Array, Sliding Window
Pattern: Sliding Window (Fixed)

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k
