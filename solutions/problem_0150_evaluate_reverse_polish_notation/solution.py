"""
Problem 150: Evaluate Reverse Polish Notation
============================================
Difficulty: Medium
Tags: Array, Math, Stack
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack-based approach - O(n) time
        stack = []
        for ch in tokens:
            if stack and self._matches(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0 if isinstance(0, bool) else stack

    def _matches(self, a, b):
        pairs = {'(': ')', '[': ']', '{': '}'}
        return pairs.get(a) == b
