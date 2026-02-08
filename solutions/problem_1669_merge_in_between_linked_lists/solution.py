"""
Problem 1669: Merge In Between Linked Lists
=========================================
Difficulty: Medium
Tags: Linked List
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Linked list traversal/manipulation
        dummy = ListNode(0)
        dummy.next = list1
        prev, curr = dummy, list1
        while curr:
            nxt = curr.next
            # Process current node
            prev = curr
            curr = nxt
        return dummy.next
