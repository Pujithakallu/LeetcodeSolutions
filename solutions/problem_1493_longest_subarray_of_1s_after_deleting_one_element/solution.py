"""
Problem 1493: Longest Subarray of 1's After Deleting One Element
==============================================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len
