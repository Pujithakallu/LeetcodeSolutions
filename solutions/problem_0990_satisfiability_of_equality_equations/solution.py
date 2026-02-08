"""
Problem 990: Satisfiability of Equality Equations
================================================
Difficulty: Medium
Tags: Array, String, Union-Find, Graph Theory
Pattern: Union-Find / Disjoint Set

Time Complexity:  O(n * alpha(n))
Space Complexity: O(n)
"""

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Union Find (Disjoint Set Union) - O(n * alpha(n))
        parent = list(range(len(equations) + 1 if isinstance(equations, list) else equations + 1))
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
