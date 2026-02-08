"""
Problem 1701: Average Waiting Time
================================
Difficulty: Medium
Tags: Array, Simulation
Pattern: Simulation

Time Complexity:  O(n) or O(n * k)
Space Complexity: O(n)
"""

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # Simulation approach - follow the rules step by step
        result = 0.0
        for i in range(len(customers) if isinstance(customers, list) else customers):
            # Simulate each step
            pass
        return result
