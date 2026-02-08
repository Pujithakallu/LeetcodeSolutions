"""
Problem 2359: Find Closest Node to Given Two Nodes
================================================
Difficulty: Medium
Tags: Depth-First Search, Graph Theory
Pattern: DFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
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
