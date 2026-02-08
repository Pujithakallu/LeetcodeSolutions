"""
Problem 1007: Minimum Domino Rotations For Equal Row
==================================================
Difficulty: Medium
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(tops)):
            if isinstance(tops[i], int):
                curr_max = max(curr_max, tops[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
