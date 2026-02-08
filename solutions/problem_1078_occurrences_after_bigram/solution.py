"""
Problem 1078: Occurrences After Bigram
====================================
Difficulty: Easy
Tags: String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # String processing approach - O(n) time
        result = []
        for ch in text:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance([], bool) else processed
