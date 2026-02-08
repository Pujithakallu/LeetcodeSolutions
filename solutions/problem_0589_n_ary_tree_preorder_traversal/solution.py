"""
Problem 589: N-ary Tree Preorder Traversal
=========================================
Difficulty: Easy
Tags: Stack, Tree, Depth-First Search
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Node:
    def __init__(self, val: Optional[int], children: Optional[List['Node']]):
        # Initialize data structure
        self.val = val
        self.children = children

    def preorder(self, root: 'Node') -> List[int]:
        return []

