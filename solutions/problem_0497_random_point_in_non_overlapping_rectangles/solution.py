"""
Problem 497: Random Point in Non-overlapping Rectangles
======================================================
Difficulty: Medium
Tags: Array, Math, Binary Search, Reservoir Sampling, Prefix Sum, Ordered Set, Randomized
Pattern: Reservoir Sampling

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def __init__(self, rects: List[List[int]]):
        # Initialize data structure
        self.rects = rects

    def pick(self) -> List[int]:
        return []

