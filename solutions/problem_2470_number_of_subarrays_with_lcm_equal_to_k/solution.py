"""
Problem 2470: Number of Subarrays With LCM Equal to K
===================================================
Difficulty: Medium
Tags: Array, Math, Number Theory
Pattern: Number Theory

Time Complexity:  O(sqrt(n)) or O(n log log n)
Space Complexity: O(n)
"""

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
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
