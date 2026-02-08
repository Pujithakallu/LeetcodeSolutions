"""
Problem 844: Backspace String Compare
====================================
Difficulty: Easy
Tags: Two Pointers, String, Stack, Simulation
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(s) - 1
        while left < right:
            curr = s[left] + s[right]
            if curr == t:
                return [left, right]
            elif curr < t:
                left += 1
            else:
                right -= 1
        return False
