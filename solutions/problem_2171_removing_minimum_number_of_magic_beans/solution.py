"""
Problem 2171: Removing Minimum Number of Magic Beans
==================================================
Difficulty: Medium
Tags: Array, Greedy, Sorting, Enumeration, Prefix Sum
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # Sort + greedy - O(n log n) time
        beans.sort()
        result = 0
        curr_end = 0
        for item in beans:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
