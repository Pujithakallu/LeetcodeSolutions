"""
Problem 821: Shortest Distance to a Character
============================================
Difficulty: Easy
Tags: Array, Two Pointers, String
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(s) - 1
        while left < right:
            curr = s[left] + s[right]
            if curr == c:
                return [left, right]
            elif curr < c:
                left += 1
            else:
                right -= 1
        return []
