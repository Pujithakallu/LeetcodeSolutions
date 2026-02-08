"""
Problem 789: Escape The Ghosts
=============================
Difficulty: Medium
Tags: Array, Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # Mathematical approach
        result = 0
        x = ghosts
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
