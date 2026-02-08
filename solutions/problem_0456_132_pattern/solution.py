"""
Problem 456: 132 Pattern
=======================
Difficulty: Medium
Tags: Array, Binary Search, Stack, Monotonic Stack, Ordered Set
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Monotonic stack - O(n) time, O(n) space
        n = len(nums)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
