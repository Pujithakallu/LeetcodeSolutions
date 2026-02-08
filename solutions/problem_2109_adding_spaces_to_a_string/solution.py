"""
Problem 2109: Adding Spaces to a String
=====================================
Difficulty: Medium
Tags: Array, Two Pointers, String, Simulation
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(s) - 1
        while left < right:
            curr = s[left] + s[right]
            if curr == spaces:
                return [left, right]
            elif curr < spaces:
                left += 1
            else:
                right -= 1
        return ""
