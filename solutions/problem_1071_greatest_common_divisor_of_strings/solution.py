"""
Problem 1071: Greatest Common Divisor of Strings
==============================================
Difficulty: Easy
Tags: Math, String
Pattern: Math / String

Time Complexity:  O(n+m)
Space Complexity: O(n+m)
"""

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        return str1[:gcd(len(str1), len(str2))]
