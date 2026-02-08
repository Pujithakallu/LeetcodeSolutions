"""
Problem 495: Teemo Attacking
===========================
Difficulty: Easy
Tags: Array, Simulation
Pattern: Simulation

Time Complexity:  O(n) or O(n * k)
Space Complexity: O(n)
"""

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # Simulation approach - follow the rules step by step
        result = 0
        for i in range(len(timeSeries) if isinstance(timeSeries, list) else timeSeries):
            # Simulate each step
            pass
        return result
