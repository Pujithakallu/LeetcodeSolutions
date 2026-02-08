"""
Problem 60: Permutation Sequence
================================
Difficulty: Hard
Tags: Math, Recursion
Pattern: Math

Time Complexity:  O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        nums = list(range(1, n+1))
        k -= 1
        result = []
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            idx = k // f
            result.append(str(nums[idx]))
            nums.pop(idx)
            k %= f
        return ''.join(result)
