"""
Problem 950: Reveal Cards In Increasing Order
============================================
Difficulty: Medium
Tags: Array, Queue, Sorting, Simulation
Pattern: Queue / BFS

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Queue-based approach - O(n) time
        from collections import deque
        queue = deque()
        for val in deck:
            queue.append(val)
        result = []
        while queue:
            result.append(queue.popleft())
        return result
