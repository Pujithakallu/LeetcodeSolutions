"""
Problem 234: Palindrome Linked List
==================================
Difficulty: Easy
Tags: Linked List, Two Pointers, Stack, Recursion
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
