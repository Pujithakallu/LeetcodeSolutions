"""
Problem 1912: Design Movie Rental System
======================================
Difficulty: Hard
Tags: Array, Hash Table, Design, Heap (Priority Queue), Ordered Set
Pattern: Ordered Set / SortedList

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        # Initialize data structure
        self.n = n
        self.entries = entries

    def search(self, movie: int) -> List[int]:
        return []

    def rent(self, shop: int, movie: int) -> None:
        return None

    def drop(self, shop: int, movie: int) -> None:
        return None

    def report(self) -> List[List[int]]:
        return []

