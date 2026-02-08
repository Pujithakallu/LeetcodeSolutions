"""
Problem 853: Car Fleet
=====================
Difficulty: Medium
Tags: Array, Stack, Sorting, Monotonic Stack
Pattern: Stack / Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        fleets = 0
        prev_time = 0
        for pos, spd in pairs:
            time = (target - pos) / spd
            if time > prev_time:
                fleets += 1
                prev_time = time
        return fleets
