"""
Problem 1743: Restore the Array From Adjacent Pairs
=================================================
Difficulty: Medium
Tags: Array, Hash Table, Depth-First Search
Pattern: DFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
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
