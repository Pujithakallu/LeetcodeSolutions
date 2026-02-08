"""
Problem 2390: Removing Stars From a String
========================================
Difficulty: Medium
Tags: String, Stack, Simulation
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
