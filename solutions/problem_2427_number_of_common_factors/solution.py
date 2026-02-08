"""
Problem 2427: Number of Common Factors
====================================
Difficulty: Easy
Tags: Math, Enumeration, Number Theory
Pattern: Number Theory

Time Complexity:  O(sqrt(n)) or O(n log log n)
Space Complexity: O(n)
"""

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Number theory approach
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        result = a[0] if isinstance(a, list) else a
        if isinstance(a, list):
            for val in a[1:]:
                result = gcd(result, val)
        return result
