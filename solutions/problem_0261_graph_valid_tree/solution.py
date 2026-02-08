"""
Problem 261: Graph Valid Tree
============================
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
Pattern: Union Find

Time Complexity:  O(n * alpha(n))
Space Complexity: O(n)
"""

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
        return True
