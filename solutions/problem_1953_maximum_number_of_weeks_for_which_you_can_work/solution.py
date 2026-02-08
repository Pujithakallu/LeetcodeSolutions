"""
Problem 1953: Maximum Number of Weeks for Which You Can Work
==========================================================
Difficulty: Medium
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(milestones)):
            if isinstance(milestones[i], int):
                curr_max = max(curr_max, milestones[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
