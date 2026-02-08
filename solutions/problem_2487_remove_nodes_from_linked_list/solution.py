"""
Problem 2487: Remove Nodes From Linked List
=========================================
Difficulty: Medium
Tags: Linked List, Stack, Recursion, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Monotonic stack - O(n) time, O(n) space
        n = len(head)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and head[i] > head[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
