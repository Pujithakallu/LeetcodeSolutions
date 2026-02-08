"""
Problem 1433: Check If a String Can Break Another String
======================================================
Difficulty: Medium
Tags: String, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        # Sort + greedy - O(n log n) time
        s1.sort()
        result = 0
        curr_end = 0
        for item in s1:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
