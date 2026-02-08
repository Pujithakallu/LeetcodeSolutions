"""
Problem 2117: Abbreviating the Product of a Range
===============================================
Difficulty: Hard
Tags: Math, Number Theory
Pattern: Number Theory

Time Complexity:  O(sqrt(n)) or O(n log log n)
Space Complexity: O(n)
"""

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        # Number theory approach
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        result = left[0] if isinstance(left, list) else left
        if isinstance(left, list):
            for val in left[1:]:
                result = gcd(result, val)
        return result
