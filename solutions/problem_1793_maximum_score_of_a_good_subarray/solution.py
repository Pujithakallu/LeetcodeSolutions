"""
Problem 1793: Maximum Score of a Good Subarray
============================================
Difficulty: Hard
Tags: Array, Two Pointers, Binary Search, Stack, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
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
