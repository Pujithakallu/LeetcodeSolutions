"""
Problem 1332: Remove Palindromic Subsequences
===========================================
Difficulty: Easy
Tags: Two Pointers, String
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(s) - 1
        while left < right:
            curr = s[left] + s[right]
            if curr == s:
                return [left, right]
            elif curr < s:
                left += 1
            else:
                right -= 1
        return 0
