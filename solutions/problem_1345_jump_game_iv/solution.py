"""
Problem 1345: Jump Game IV
========================
Difficulty: Hard
Tags: Array, Hash Table, Breadth-First Search
Pattern: BFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # BFS on graph - O(V+E) time
        from collections import deque
        if not arr:
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
