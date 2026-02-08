"""
Problem 1813: Sentence Similarity III
===================================
Difficulty: Medium
Tags: Array, Two Pointers, String
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(sentence1) - 1
        while left < right:
            curr = sentence1[left] + sentence1[right]
            if curr == sentence2:
                return [left, right]
            elif curr < sentence2:
                left += 1
            else:
                right -= 1
        return False
