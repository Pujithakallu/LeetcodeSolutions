"""
Problem 2491: Divide Players Into Teams of Equal Skill
====================================================
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, Sorting
Pattern: Two Pointers on Sorted Array

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Sort + two pointers - O(n log n) time
        skill.sort()
        left, right = 0, len(skill) - 1
        result = 0
        while left < right:
            curr_sum = skill[left] + skill[right]
            if curr_sum < skill if isinstance(skill, int) else 0:
                left += 1
            else:
                right -= 1
        return result
