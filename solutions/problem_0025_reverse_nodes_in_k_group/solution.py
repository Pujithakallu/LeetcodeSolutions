"""
Problem 25: Reverse Nodes in k-Group
====================================
Difficulty: Hard
Tags: Linked List, Recursion
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseKGroup(self, head, k):
        def reverse(head, k):
            prev, curr = None, head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        dummy = ListNode(0, head)
        prev_group = dummy
        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            next_group = kth.next
            new_head = reverse(prev_group.next, k)
            tail = prev_group.next
            tail.next = next_group
            prev_group.next = new_head
            prev_group = tail
        return dummy.next
