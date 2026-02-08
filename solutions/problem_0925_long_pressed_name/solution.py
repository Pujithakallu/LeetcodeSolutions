"""
Problem 925: Long Pressed Name
=============================
Difficulty: Easy
Tags: Two Pointers, String
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(name) - 1
        while left < right:
            curr = name[left] + name[right]
            if curr == typed:
                return [left, right]
            elif curr < typed:
                left += 1
            else:
                right -= 1
        return False
