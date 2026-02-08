"""
Problem 809: Expressive Words
============================
Difficulty: Medium
Tags: Array, Two Pointers, String
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(s) - 1
        while left < right:
            curr = s[left] + s[right]
            if curr == words:
                return [left, right]
            elif curr < words:
                left += 1
            else:
                right -= 1
        return 0
