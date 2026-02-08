"""
Problem 365: Water and Jug Problem
=================================
Difficulty: Medium
Tags: Math, Depth-First Search, Breadth-First Search
Pattern: DFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
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
        return result if isinstance(False, list) else len(result)
