"""
Problem 1625: Lexicographically Smallest String After Applying Operations
=======================================================================
Difficulty: Medium
Tags: String, Depth-First Search, Breadth-First Search, Enumeration
Pattern: DFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
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
        return result if isinstance("", list) else len(result)
