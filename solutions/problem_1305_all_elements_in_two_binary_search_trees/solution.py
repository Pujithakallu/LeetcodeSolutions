"""
Problem 1305: All Elements in Two Binary Search Trees
===================================================
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Search Tree, Sorting, Binary Tree
Pattern: Binary Search Tree

Time Complexity:  O(h)
Space Complexity: O(h)
"""

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        # BST search/insert - O(h) time
        def search(node, target):
            if not node:
                return None
            if target == node.val:
                return node
            elif target < node.val:
                return search(node.left, target)
            else:
                return search(node.right, target)
        return search(root1, root2 if 'root2' != 'root1' else 0)
