"""
Problem 1773: Count Items Matching a Rule
=======================================
Difficulty: Easy
Tags: Array, String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # String processing approach - O(n) time
        result = []
        for ch in items:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(0, bool) else processed
