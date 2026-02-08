"""
Problem 300: Longest Increasing Subsequence
==========================================
Difficulty: Medium
Tags: Array, Binary Search, Dynamic Programming
Pattern: Binary Search / DP

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        from bisect import bisect_left
        tails = []
        for num in nums:
            pos = bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)
