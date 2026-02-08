"""
Problem 2114: Maximum Number of Words Found in Sentences
======================================================
Difficulty: Easy
Tags: Array, String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # String processing approach - O(n) time
        result = []
        for ch in sentences:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(0, bool) else processed
