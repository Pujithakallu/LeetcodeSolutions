"""
Problem 2326: Spiral Matrix IV
============================
Difficulty: Medium
Tags: Array, Linked List, Matrix, Simulation
Pattern: Linked List

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Linked list traversal/manipulation
        dummy = ListNode(0)
        dummy.next = m
        prev, curr = dummy, m
        while curr:
            nxt = curr.next
            # Process current node
            prev = curr
            curr = nxt
        return dummy.next
