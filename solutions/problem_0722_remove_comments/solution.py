"""
Problem 722: Remove Comments
===========================
Difficulty: Medium
Tags: Array, String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # String processing approach - O(n) time
        result = []
        for ch in source:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance([], bool) else processed
