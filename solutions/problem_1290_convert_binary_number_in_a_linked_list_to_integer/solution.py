"""
Problem 1290: Convert Binary Number in a Linked List to Integer
=============================================================
Difficulty: Easy
Tags: Linked List, Math
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
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
