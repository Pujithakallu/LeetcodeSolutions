"""
Problem 2105: Watering Plants II
==============================
Difficulty: Medium
Tags: Array, Two Pointers, Simulation
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(plants) - 1
        while left < right:
            curr = plants[left] + plants[right]
            if curr == capacityA:
                return [left, right]
            elif curr < capacityA:
                left += 1
            else:
                right -= 1
        return 0
