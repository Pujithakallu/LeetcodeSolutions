"""
Problem 65: Valid Number
========================
Difficulty: Hard
Tags: String
Pattern: String Parsing / State Machine

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False
