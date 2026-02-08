"""
Problem 2130: Maximum Twin Sum of a Linked List
=============================================
Difficulty: Medium
Tags: Linked List, Two Pointers, Stack
Pattern: Linked List / Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def pairSum(self, head) -> int:
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse second half
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        # Find max twin sum
        max_sum = 0
        while prev:
            max_sum = max(max_sum, head.val + prev.val)
            head = head.next
            prev = prev.next
        return max_sum
