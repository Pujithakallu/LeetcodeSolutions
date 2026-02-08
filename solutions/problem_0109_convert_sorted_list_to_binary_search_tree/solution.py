"""
Problem 109: Convert Sorted List to Binary Search Tree
=====================================================
Difficulty: Medium
Tags: Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
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
