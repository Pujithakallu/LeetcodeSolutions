"""
Problem 975: Odd Even Jump
=========================
Difficulty: Hard
Tags: Array, Dynamic Programming, Stack, Sorting, Monotonic Stack, Ordered Set
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # Monotonic stack - O(n) time, O(n) space
        n = len(arr)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and arr[i] > arr[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
