"""
Problem 636: Exclusive Time of Functions
=======================================
Difficulty: Medium
Tags: Array, Stack
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # Stack-based approach - O(n) time
        stack = []
        for ch in n:
            if stack and self._matches(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0 if isinstance([], bool) else stack

    def _matches(self, a, b):
        pairs = {'(': ')', '[': ']', '{': '}'}
        return pairs.get(a) == b
