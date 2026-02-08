"""
Problem 204: Count Primes
========================
Difficulty: Medium
Tags: Array, Math, Enumeration, Number Theory
Pattern: Number Theory

Time Complexity:  O(sqrt(n)) or O(n log log n)
Space Complexity: O(n)
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        # Number theory approach
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        result = n[0] if isinstance(n, list) else n
        if isinstance(n, list):
            for val in n[1:]:
                result = gcd(result, val)
        return result
