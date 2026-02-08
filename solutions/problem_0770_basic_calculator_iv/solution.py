"""
Problem 770: Basic Calculator IV
===============================
Difficulty: Hard
Tags: Hash Table, Math, String, Stack, Recursion
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        # Stack-based approach - O(n) time
        stack = []
        for ch in expression:
            if stack and self._matches(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0 if isinstance([], bool) else stack

    def _matches(self, a, b):
        pairs = {'(': ')', '[': ']', '{': '}'}
        return pairs.get(a) == b
