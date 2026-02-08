"""
Problem 107: Binary Tree Level Order Traversal II
================================================
Difficulty: Medium
Tags: Tree, Breadth-First Search, Binary Tree
Pattern: BFS Level-Order Traversal

Time Complexity:  O(n)
Space Complexity: O(w)
"""

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS level-order traversal - O(n) time, O(n) space
        from collections import deque
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
