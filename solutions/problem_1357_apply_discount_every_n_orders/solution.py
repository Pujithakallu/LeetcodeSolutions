"""
Problem 1357: Apply Discount Every n Orders
=========================================
Difficulty: Medium
Tags: Array, Hash Table, Design
Pattern: Design

Time Complexity:  O(1) per operation
Space Complexity: O(n)
"""

class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        # Initialize data structure
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices

    def getBill(self, product: List[int], amount: List[int]) -> float:
        return 0.0

