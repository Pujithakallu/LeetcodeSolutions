"""
Problem 735: Asteroid Collision
==============================
Difficulty: Medium
Tags: Array, Stack, Simulation
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Stack-based approach - O(n) time
        stack = []
        for ch in asteroids:
            if stack and self._matches(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0 if isinstance([], bool) else stack

    def _matches(self, a, b):
        pairs = {'(': ')', '[': ']', '{': '}'}
        return pairs.get(a) == b
