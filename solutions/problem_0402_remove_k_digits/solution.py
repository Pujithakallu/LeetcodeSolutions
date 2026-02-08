"""
Problem 402: Remove K Digits
===========================
Difficulty: Medium
Tags: String, Stack, Greedy, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Monotonic stack - O(n) time, O(n) space
        n = len(num)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and num[i] > num[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
