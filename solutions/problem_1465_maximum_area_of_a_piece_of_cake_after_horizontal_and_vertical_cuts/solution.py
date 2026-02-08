"""
Problem 1465: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
==============================================================================
Difficulty: Medium
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Sort + greedy - O(n log n) time
        h.sort()
        result = 0
        curr_end = 0
        for item in h:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
