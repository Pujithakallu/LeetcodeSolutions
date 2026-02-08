"""
Problem 1157: Online Majority Element In Subarray
===============================================
Difficulty: Hard
Tags: Array, Binary Search, Design, Binary Indexed Tree, Segment Tree
Pattern: Segment Tree

Time Complexity:  O(n log n) build, O(log n) query/update
Space Complexity: O(n)
"""

class MajorityChecker:
    def __init__(self, arr: List[int]):
        # Initialize data structure
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        return 0

