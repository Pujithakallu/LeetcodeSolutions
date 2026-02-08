"""
Problem 2244: Minimum Rounds to Complete All Tasks
================================================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Counting
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(tasks)):
            if isinstance(tasks[i], int):
                curr_max = max(curr_max, tasks[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
