"""
Problem 797: All Paths From Source to Target
===========================================
Difficulty: Medium
Tags: Backtracking, Depth-First Search, Breadth-First Search, Graph Theory
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(graph)):
                path.append(graph[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
