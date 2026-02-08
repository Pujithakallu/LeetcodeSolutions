"""
Problem 141: Linked List Cycle
=============================
Difficulty: Easy
Tags: Hash Table, Linked List, Two Pointers
Pattern: Fast and Slow Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def hasCycle(self, head) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
