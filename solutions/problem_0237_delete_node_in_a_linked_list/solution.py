"""
Problem 237: Delete Node in a Linked List
========================================
Difficulty: Medium
Tags: Linked List
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def deleteNode(self, node: int) -> None:
        # Linked list traversal/manipulation
        dummy = ListNode(0)
        dummy.next = node
        prev, curr = dummy, node
        while curr:
            nxt = curr.next
            # Process current node
            prev = curr
            curr = nxt
        return dummy.next
