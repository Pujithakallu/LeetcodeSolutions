"""
Problem 1921: Eliminate Maximum Number of Monsters
================================================
Difficulty: Medium
Tags: Array, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Sort + greedy - O(n log n) time
        dist.sort()
        result = 0
        curr_end = 0
        for item in dist:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
