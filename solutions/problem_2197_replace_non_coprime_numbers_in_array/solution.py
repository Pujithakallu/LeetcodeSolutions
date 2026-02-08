"""
Problem 2197: Replace Non-Coprime Numbers in Array
================================================
Difficulty: Hard
Tags: Array, Math, Stack, Number Theory
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # Stack-based approach - O(n) time
        stack = []
        for ch in nums:
            if stack and self._matches(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0 if isinstance([], bool) else stack

    def _matches(self, a, b):
        pairs = {'(': ')', '[': ']', '{': '}'}
        return pairs.get(a) == b
