"""
Problem 2353: Design a Food Rating System
=======================================
Difficulty: Medium
Tags: Array, Hash Table, String, Design, Heap (Priority Queue), Ordered Set
Pattern: Ordered Set / SortedList

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Initialize data structure
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

    def changeRating(self, food: str, newRating: int) -> None:
        return None

    def highestRated(self, cuisine: str) -> str:
        return ""

