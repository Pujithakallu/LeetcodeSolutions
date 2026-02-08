"""
Problem 1629: Slowest Key
=======================
Difficulty: Easy
Tags: Array, String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # String processing approach - O(n) time
        result = []
        for ch in releaseTimes:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance("", bool) else processed
