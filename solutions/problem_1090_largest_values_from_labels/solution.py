"""
Problem 1090: Largest Values From Labels
======================================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting, Counting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # Sort + greedy - O(n log n) time
        values.sort()
        result = 0
        curr_end = 0
        for item in values:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
