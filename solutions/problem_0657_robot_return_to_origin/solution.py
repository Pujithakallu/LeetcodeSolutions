"""
Problem 657: Robot Return to Origin
==================================
Difficulty: Easy
Tags: String, Simulation
Pattern: Simulation

Time Complexity:  O(n) or O(n * k)
Space Complexity: O(n)
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Simulation approach - follow the rules step by step
        result = False
        for i in range(len(moves) if isinstance(moves, list) else moves):
            # Simulate each step
            pass
        return result
