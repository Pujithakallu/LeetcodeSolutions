"""
Problem 1367: Linked List in Binary Tree
======================================
Difficulty: Medium
Tags: Linked List, Tree, Depth-First Search, Binary Tree
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Linked list traversal/manipulation
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            nxt = curr.next
            # Process current node
            prev = curr
            curr = nxt
        return dummy.next
