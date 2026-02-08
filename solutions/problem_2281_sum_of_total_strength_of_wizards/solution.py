"""
Problem 2281: Sum of Total Strength of Wizards
============================================
Difficulty: Hard
Tags: Array, Stack, Monotonic Stack, Prefix Sum
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        # Monotonic stack - O(n) time, O(n) space
        n = len(strength)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and strength[i] > strength[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
