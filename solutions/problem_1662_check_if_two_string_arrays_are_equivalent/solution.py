"""
Problem 1662: Check If Two String Arrays are Equivalent
=====================================================
Difficulty: Easy
Tags: Array, String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # String processing approach - O(n) time
        result = []
        for ch in word1:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(False, bool) else processed
