"""
Problem 1616: Split Two Strings to Make Palindrome
================================================
Difficulty: Medium
Tags: Two Pointers, String
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(a) - 1
        while left < right:
            curr = a[left] + a[right]
            if curr == b:
                return [left, right]
            elif curr < b:
                left += 1
            else:
                right -= 1
        return False
