"""
Problem 114: Flatten Binary Tree to Linked List
==============================================
Difficulty: Medium
Tags: Linked List, Stack, Tree, Depth-First Search, Binary Tree
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Linked list traversal/manipulation
        dummy = ListNode(0)
        dummy.next = root
        prev, curr = dummy, root
        while curr:
            nxt = curr.next
            # Process current node
            prev = curr
            curr = nxt
        return dummy.next
