"""
Problem 721: Accounts Merge
==========================
Difficulty: Medium
Tags: Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find, Sorting
Pattern: Union-Find / Disjoint Set

Time Complexity:  O(n * alpha(n))
Space Complexity: O(n)
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union Find (Disjoint Set Union) - O(n * alpha(n))
        parent = list(range(len(accounts) + 1 if isinstance(accounts, list) else accounts + 1))
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
