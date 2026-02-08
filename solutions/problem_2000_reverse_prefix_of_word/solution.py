"""
Problem 2000: Reverse Prefix of Word
==================================
Difficulty: Easy
Tags: Two Pointers, String, Stack
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(word) - 1
        while left < right:
            curr = word[left] + word[right]
            if curr == ch:
                return [left, right]
            elif curr < ch:
                left += 1
            else:
                right -= 1
        return ""
