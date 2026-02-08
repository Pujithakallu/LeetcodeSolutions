"""
Problem 1042: Flower Planting With No Adjacent
============================================
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Graph Theory
Pattern: DFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # DFS on graph - O(V+E) time
        visited = set()
        result = []
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            result.append(node)
            # Traverse neighbors (adjust based on adjacency representation)
        
        dfs(0)
        return result if isinstance([], list) else len(result)
