"""
Problem 1061: Lexicographically Smallest Equivalent String
========================================================
Difficulty: Medium
Tags: String, Union-Find
Pattern: Union-Find / Disjoint Set

Time Complexity:  O(n * alpha(n))
Space Complexity: O(n)
"""

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Union Find (Disjoint Set Union) - O(n * alpha(n))
        parent = list(range(len(s1) + 1 if isinstance(s1, list) else s1 + 1))
        rank = [0] * len(parent)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        
        components = len(parent)
        # Process edges/connections
        return components
