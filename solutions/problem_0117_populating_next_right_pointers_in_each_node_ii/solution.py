"""
Problem 117: Populating Next Right Pointers in Each Node II
==========================================================
Difficulty: Medium
Tags: Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, val: int, left: 'Node', right: 'Node', next: 'Node'):
        # Initialize data structure
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def connect(self, root: 'Node') -> 'Node':
        return None

