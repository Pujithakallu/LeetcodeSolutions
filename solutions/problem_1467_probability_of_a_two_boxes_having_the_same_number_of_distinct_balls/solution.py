"""
Problem 1467: Probability of a Two Boxes Having The Same Number of Distinct Balls
===============================================================================
Difficulty: Hard
Tags: Array, Math, Dynamic Programming, Backtracking, Combinatorics, Probability and Statistics
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(balls)):
                path.append(balls[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
