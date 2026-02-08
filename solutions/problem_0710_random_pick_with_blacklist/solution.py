"""
Problem 710: Random Pick with Blacklist
======================================
Difficulty: Hard
Tags: Array, Hash Table, Math, Binary Search, Sorting, Randomized
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        # Initialize data structure
        self.n = n
        self.blacklist = blacklist

    def pick(self) -> int:
        return 0

