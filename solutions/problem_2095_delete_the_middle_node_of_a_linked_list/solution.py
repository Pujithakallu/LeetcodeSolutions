"""
Problem 2095: Delete the Middle Node of a Linked List
===================================================
Difficulty: Medium
Tags: Linked List, Two Pointers
Pattern: Linked List / Fast-Slow Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def deleteMiddle(self, head):
        if not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
