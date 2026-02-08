"""
Problem 2446: Determine if Two Events Have Conflict
=================================================
Difficulty: Easy
Tags: Array, String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # String processing approach - O(n) time
        result = []
        for ch in event1:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(False, bool) else processed
