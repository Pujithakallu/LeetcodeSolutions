"""
Problem 1557: Minimum Number of Vertices to Reach All Nodes
=========================================================
Difficulty: Medium
Tags: Graph Theory
Pattern: Graph / Indegree

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges) -> list[int]:
        has_incoming = set()
        for _, v in edges:
            has_incoming.add(v)
        return [i for i in range(n) if i not in has_incoming]
