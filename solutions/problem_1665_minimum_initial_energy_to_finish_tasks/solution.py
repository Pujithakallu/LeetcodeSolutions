"""
Problem 1665: Minimum Initial Energy to Finish Tasks
==================================================
Difficulty: Hard
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort + greedy - O(n log n) time
        tasks.sort()
        result = 0
        curr_end = 0
        for item in tasks:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
