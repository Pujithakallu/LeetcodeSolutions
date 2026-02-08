"""
Problem 1171: Remove Zero Sum Consecutive Nodes from Linked List
==============================================================
Difficulty: Medium
Tags: Hash Table, Linked List
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
