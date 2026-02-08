"""
Problem 1319: Number of Operations to Make Network Connected
==========================================================
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
Pattern: Union-Find

Time Complexity:  O(n + E * alpha(n))
Space Complexity: O(n)
"""

class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        components = n
        for a, b in connections:
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb
                components -= 1
        return components - 1
