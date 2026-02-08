"""
Problem 2059: Minimum Operations to Convert Number
================================================
Difficulty: Medium
Tags: Array, Breadth-First Search
Pattern: BFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        # BFS on graph - O(V+E) time
        from collections import deque
        if not nums:
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
