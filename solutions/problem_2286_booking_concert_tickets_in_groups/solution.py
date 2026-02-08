"""
Problem 2286: Booking Concert Tickets in Groups
=============================================
Difficulty: Hard
Tags: Binary Search, Design, Binary Indexed Tree, Segment Tree
Pattern: Segment Tree

Time Complexity:  O(n log n) build, O(log n) query/update
Space Complexity: O(n)
"""

class BookMyShow:
    def __init__(self, n: int, m: int):
        # Initialize data structure
        self.n = n
        self.m = m

    def gather(self, k: int, maxRow: int) -> List[int]:
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        return False

