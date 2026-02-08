"""
Problem 2108: Find First Palindromic String in the Array
======================================================
Difficulty: Easy
Tags: Array, Two Pointers, String
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(words) - 1
        while left < right:
            curr = words[left] + words[right]
            if curr == words:
                return [left, right]
            elif curr < words:
                left += 1
            else:
                right -= 1
        return ""
