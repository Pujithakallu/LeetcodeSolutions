"""
Problem 1808: Maximize Number of Nice Divisors
============================================
Difficulty: Hard
Tags: Math, Recursion, Number Theory
Pattern: Number Theory

Time Complexity:  O(sqrt(n)) or O(n log log n)
Space Complexity: O(n)
"""

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        # Number theory approach
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        result = primeFactors[0] if isinstance(primeFactors, list) else primeFactors
        if isinstance(primeFactors, list):
            for val in primeFactors[1:]:
                result = gcd(result, val)
        return result
