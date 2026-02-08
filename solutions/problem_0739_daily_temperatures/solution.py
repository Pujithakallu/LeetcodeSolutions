"""
Problem 739: Daily Temperatures
==============================
Difficulty: Medium
Tags: Array, Stack, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result
