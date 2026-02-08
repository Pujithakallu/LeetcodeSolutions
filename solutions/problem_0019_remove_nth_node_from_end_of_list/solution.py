"""
Problem 19: Remove Nth Node From End of List
============================================
Difficulty: Medium
Tags: Linked List, Two Pointers
Pattern: Fast and Slow Pointers

Time Complexity:  O(L) where L = list length
Space Complexity: O(1)
"""

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
