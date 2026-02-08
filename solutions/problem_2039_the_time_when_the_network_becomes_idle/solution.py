"""
Problem 2039: The Time When the Network Becomes Idle
==================================================
Difficulty: Medium
Tags: Array, Breadth-First Search, Graph Theory
Pattern: BFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # BFS on graph - O(V+E) time
        from collections import deque
        if not edges:
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
