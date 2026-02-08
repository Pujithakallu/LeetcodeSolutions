"""
Problem 2211: Count Collisions on a Road
======================================
Difficulty: Medium
Tags: String, Stack, Simulation
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countCollisions(self, directions: str) -> int:
        # Stack-based approach - O(n) time
        stack = []
        for ch in directions:
            if stack and self._matches(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0 if isinstance(0, bool) else stack

    def _matches(self, a, b):
        pairs = {'(': ')', '[': ']', '{': '}'}
        return pairs.get(a) == b
