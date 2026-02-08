"""
Problem 387: First Unique Character in a String
==============================================
Difficulty: Easy
Tags: Hash Table, String, Queue, Counting
Pattern: Queue / BFS

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Queue-based approach - O(n) time
        from collections import deque
        queue = deque()
        for val in s:
            queue.append(val)
        result = []
        while queue:
            result.append(queue.popleft())
        return result
