"""
Problem 169: Majority Element
============================
Difficulty: Easy
Tags: Array, Hash Table, Divide and Conquer, Sorting, Counting
Pattern: Boyer-Moore Voting

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
