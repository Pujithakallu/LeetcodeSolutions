"""
Problem 641: Design Circular Deque
=================================
Difficulty: Medium
Tags: Array, Linked List, Design, Queue
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class MyCircularDeque:
    def __init__(self, k: int):
        # Initialize data structure
        self.k = k

    def insertFront(self, value: int) -> bool:
        return False

    def insertLast(self, value: int) -> bool:
        return False

    def deleteFront(self) -> bool:
        return False

    def deleteLast(self) -> bool:
        return False

    def getFront(self) -> int:
        return 0

    def getRear(self) -> int:
        return 0

    def isEmpty(self) -> bool:
        return False

    def isFull(self) -> bool:
        return False

