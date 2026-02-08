"""
Problem 429: N-ary Tree Level Order Traversal
============================================
Difficulty: Medium
Tags: Tree, Breadth-First Search
Pattern: BFS Level-Order Traversal

Time Complexity:  O(n)
Space Complexity: O(w)
"""

class Node:
    def __init__(self, val: Optional[int], children: Optional[List['Node']]):
        # Initialize data structure
        self.val = val
        self.children = children

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        return []

