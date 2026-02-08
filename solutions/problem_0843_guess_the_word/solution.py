"""
Problem 843: Guess the Word
==========================
Difficulty: Hard
Tags: Array, Math, String, Interactive, Game Theory
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        # Mathematical approach
        result = 0
        x = words
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
