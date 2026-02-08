"""
Problem 430: Flatten a Multilevel Doubly Linked List
===================================================
Difficulty: Medium
Tags: Linked List, Depth-First Search, Doubly-Linked List
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, val: int, prev: int, next: int, child: int):
        # Initialize data structure
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return None

