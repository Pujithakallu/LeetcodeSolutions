"""
Problem 1306: Jump Game III
=========================
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search
Pattern: DFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
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
