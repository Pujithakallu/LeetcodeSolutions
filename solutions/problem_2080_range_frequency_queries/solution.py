"""
Problem 2080: Range Frequency Queries
===================================
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Design, Segment Tree
Pattern: Segment Tree

Time Complexity:  O(n log n) build, O(log n) query/update
Space Complexity: O(n)
"""

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        # Initialize data structure
        self.arr = arr

    def query(self, left: int, right: int, value: int) -> int:
        return 0

