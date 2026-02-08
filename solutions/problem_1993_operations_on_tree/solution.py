"""
Problem 1993: Operations on Tree
==============================
Difficulty: Medium
Tags: Array, Hash Table, Tree, Depth-First Search, Breadth-First Search, Design
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class LockingTree:
    def __init__(self, parent: List[int]):
        # Initialize data structure
        self.parent = parent

    def lock(self, num: int, user: int) -> bool:
        return False

    def unlock(self, num: int, user: int) -> bool:
        return False

    def upgrade(self, num: int, user: int) -> bool:
        return False

