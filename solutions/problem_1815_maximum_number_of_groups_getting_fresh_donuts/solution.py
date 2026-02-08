"""
Problem 1815: Maximum Number of Groups Getting Fresh Donuts
=========================================================
Difficulty: Hard
Tags: Array, Dynamic Programming, Bit Manipulation, Memoization, Bitmask
Pattern: Dynamic Programming (Bitmask)

Time Complexity:  O(2^n * n)
Space Complexity: O(2^n)
"""

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        # Bitmask DP - O(2^n * n) time
        n = len(batchSize)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            bits = bin(mask).count('1')
            for i in range(n):
                if mask & (1 << i):
                    continue
                new_mask = mask | (1 << i)
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
        return dp[(1 << n) - 1]
