"""
Problem 455: Assign Cookies
==========================
Difficulty: Easy
Tags: Array, Two Pointers, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort + greedy - O(n log n) time
        g.sort()
        result = 0
        curr_end = 0
        for item in g:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
