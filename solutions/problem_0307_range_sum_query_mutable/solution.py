"""
Problem 307: Range Sum Query - Mutable
=====================================
Difficulty: Medium
Tags: Array, Divide and Conquer, Design, Binary Indexed Tree, Segment Tree
Pattern: Segment Tree

Time Complexity:  O(n log n) build, O(log n) query/update
Space Complexity: O(n)
"""

class NumArray:
    def __init__(self, nums: List[int]):
        # Initialize data structure
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        return None

    def sumRange(self, left: int, right: int) -> int:
        return 0

