"""
Problem 1250: Check If It Is a Good Array
=======================================
Difficulty: Hard
Tags: Array, Math, Number Theory
Pattern: Number Theory

Time Complexity:  O(sqrt(n)) or O(n log log n)
Space Complexity: O(n)
"""

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # Number theory approach
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        result = nums[0] if isinstance(nums, list) else nums
        if isinstance(nums, list):
            for val in nums[1:]:
                result = gcd(result, val)
        return result
