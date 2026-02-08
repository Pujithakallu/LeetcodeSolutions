"""
Problem 1455: Check If a Word Occurs As a Prefix of Any Word in a Sentence
========================================================================
Difficulty: Easy
Tags: Two Pointers, String, String Matching
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(sentence) - 1
        while left < right:
            curr = sentence[left] + sentence[right]
            if curr == searchWord:
                return [left, right]
            elif curr < searchWord:
                left += 1
            else:
                right -= 1
        return 0
