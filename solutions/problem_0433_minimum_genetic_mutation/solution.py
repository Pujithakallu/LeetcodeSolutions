"""
Problem 433: Minimum Genetic Mutation
====================================
Difficulty: Medium
Tags: Hash Table, String, Breadth-First Search
Pattern: BFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # BFS on graph - O(V+E) time
        from collections import deque
        if not startGene:
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
