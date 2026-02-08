"""
Problem 130: Surrounded Regions
==============================
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
Pattern: Union-Find / Disjoint Set

Time Complexity:  O(n * alpha(n))
Space Complexity: O(n)
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Union Find (Disjoint Set Union) - O(n * alpha(n))
        parent = list(range(len(board) + 1 if isinstance(board, list) else board + 1))
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
