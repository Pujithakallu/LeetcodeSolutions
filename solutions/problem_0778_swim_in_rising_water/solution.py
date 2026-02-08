"""
Problem 778: Swim in Rising Water
================================
Difficulty: Hard
Tags: Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix
Pattern: Union-Find / Disjoint Set

Time Complexity:  O(n * alpha(n))
Space Complexity: O(n)
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Union Find (Disjoint Set Union) - O(n * alpha(n))
        parent = list(range(len(grid) + 1 if isinstance(grid, list) else grid + 1))
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
