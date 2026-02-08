"""
Problem 746: Min Cost Climbing Stairs
====================================
Difficulty: Easy
Tags: Array, Dynamic Programming
Pattern: Dynamic Programming

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
