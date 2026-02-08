"""
Problem 1483: Kth Ancestor of a Tree Node
=======================================
Difficulty: Hard
Tags: Binary Search, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search, Breadth-First Search, Design
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        # Initialize data structure
        self.n = n
        self.parent = parent

    def getKthAncestor(self, node: int, k: int) -> int:
        return 0

