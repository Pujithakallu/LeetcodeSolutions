"""
Problem 2454: Next Greater Element IV
===================================
Difficulty: Hard
Tags: Array, Binary Search, Stack, Sorting, Heap (Priority Queue), Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
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
