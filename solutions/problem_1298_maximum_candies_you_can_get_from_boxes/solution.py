"""
Problem 1298: Maximum Candies You Can Get from Boxes
==================================================
Difficulty: Hard
Tags: Array, Breadth-First Search, Graph Theory
Pattern: BFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # BFS on graph - O(V+E) time
        from collections import deque
        if not status:
            return 0
        visited = set()
        queue = deque([0])
        visited.add(0)
        dist = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                # Process node
            dist += 1
        return dist
