"""
Problem 1776: Car Fleet II
========================
Difficulty: Hard
Tags: Array, Math, Stack, Heap (Priority Queue), Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # Monotonic stack - O(n) time, O(n) space
        n = len(cars)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and cars[i] > cars[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
