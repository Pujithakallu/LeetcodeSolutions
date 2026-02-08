"""
Problem 1466: Reorder Routes to Make All Paths Lead to the City Zero
==================================================================
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Graph Theory
Pattern: DFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
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
