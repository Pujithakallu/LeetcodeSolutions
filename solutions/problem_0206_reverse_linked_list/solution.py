"""
Problem 206: Reverse Linked List
===============================
Difficulty: Easy
Tags: Linked List, Recursion
Pattern: Linked List Reversal

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
