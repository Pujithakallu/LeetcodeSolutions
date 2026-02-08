"""
Problem 1967: Number of Strings That Appear as Substrings in Word
===============================================================
Difficulty: Easy
Tags: Array, String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # String processing approach - O(n) time
        result = []
        for ch in patterns:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(0, bool) else processed
