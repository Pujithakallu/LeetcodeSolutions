"""
Problem 138: Copy List with Random Pointer
=========================================
Difficulty: Medium
Tags: Hash Table, Linked List
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, x: int, next: 'Node', random: 'Node'):
        # Initialize data structure
        self.x = x
        self.next = next
        self.random = random

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return None

