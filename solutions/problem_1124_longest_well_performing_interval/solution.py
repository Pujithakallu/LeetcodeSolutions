"""
Problem 1124: Longest Well-Performing Interval
============================================
Difficulty: Medium
Tags: Array, Hash Table, Stack, Monotonic Stack, Prefix Sum
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # Monotonic stack - O(n) time, O(n) space
        n = len(hours)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and hours[i] > hours[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
