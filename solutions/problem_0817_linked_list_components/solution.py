"""
Problem 817: Linked List Components
==================================
Difficulty: Medium
Tags: Array, Hash Table, Linked List
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
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
