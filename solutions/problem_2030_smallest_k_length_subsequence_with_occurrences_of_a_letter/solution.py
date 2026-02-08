"""
Problem 2030: Smallest K-Length Subsequence With Occurrences of a Letter
======================================================================
Difficulty: Hard
Tags: String, Stack, Greedy, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        # Monotonic stack - O(n) time, O(n) space
        n = len(s)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and s[i] > s[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
