"""
Problem 1700: Number of Students Unable to Eat Lunch
==================================================
Difficulty: Easy
Tags: Array, Stack, Queue, Simulation
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Stack-based approach - O(n) time
        stack = []
        for ch in students:
            if stack and self._matches(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0 if isinstance(0, bool) else stack

    def _matches(self, a, b):
        pairs = {'(': ')', '[': ']', '{': '}'}
        return pairs.get(a) == b
