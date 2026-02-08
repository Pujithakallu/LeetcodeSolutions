"""
Problem 2162: Minimum Cost to Set Cooking Time
============================================
Difficulty: Medium
Tags: Math, Enumeration
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # Mathematical approach
        result = 0
        x = startAt
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
