"""
Problem 341: Flatten Nested List Iterator
========================================
Difficulty: Medium
Tags: Stack, Tree, Depth-First Search, Design, Queue, Iterator
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Initialize data structure
        self.nestedList = nestedList

    def next(self) -> int:
        return 0

    def hasNext(self) -> bool:
        return False

