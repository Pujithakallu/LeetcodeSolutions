"""
Problem 1019: Next Greater Node In Linked List
============================================
Difficulty: Medium
Tags: Array, Linked List, Stack, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
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
