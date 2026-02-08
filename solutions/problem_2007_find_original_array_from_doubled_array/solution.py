"""
Problem 2007: Find Original Array From Doubled Array
==================================================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # Sort + greedy - O(n log n) time
        changed.sort()
        result = 0
        curr_end = 0
        for item in changed:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
