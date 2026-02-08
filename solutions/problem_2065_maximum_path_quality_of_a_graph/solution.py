"""
Problem 2065: Maximum Path Quality of a Graph
===========================================
Difficulty: Hard
Tags: Array, Backtracking, Graph Theory
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(values)):
                path.append(values[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
