"""
Problem 876: Middle of the Linked List
=====================================
Difficulty: Easy
Tags: Linked List, Two Pointers
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
