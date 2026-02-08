"""
Problem 1944: Number of Visible People in a Queue
===============================================
Difficulty: Hard
Tags: Array, Stack, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # Monotonic stack - O(n) time, O(n) space
        n = len(heights)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and heights[i] > heights[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
