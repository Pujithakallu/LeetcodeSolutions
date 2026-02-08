"""
Problem 394: Decode String
=========================
Difficulty: Medium
Tags: String, Stack, Recursion
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def decodeString(self, s: str) -> str:
        # Stack-based approach - O(n) time
        stack = []
        for ch in s:
            if stack and self._matches(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0 if isinstance("", bool) else stack

    def _matches(self, a, b):
        pairs = {'(': ')', '[': ']', '{': '}'}
        return pairs.get(a) == b
