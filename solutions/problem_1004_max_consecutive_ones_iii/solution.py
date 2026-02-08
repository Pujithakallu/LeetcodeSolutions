"""
Problem 1004: Max Consecutive Ones III
====================================
Difficulty: Medium
Tags: Array, Binary Search, Sliding Window, Prefix Sum
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
