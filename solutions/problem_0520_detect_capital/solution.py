"""
Problem 520: Detect Capital
==========================
Difficulty: Easy
Tags: String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # String processing approach - O(n) time
        result = []
        for ch in word:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(False, bool) else processed
