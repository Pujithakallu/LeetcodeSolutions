"""
Problem 92: Reverse Linked List II
==================================
Difficulty: Medium
Tags: Linked List
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
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
