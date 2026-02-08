"""
Problem 2101: Detonate the Maximum Bombs
======================================
Difficulty: Medium
Tags: Array, Math, Depth-First Search, Breadth-First Search, Graph Theory, Geometry
Pattern: DFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
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
        return result if isinstance(0, list) else len(result)
