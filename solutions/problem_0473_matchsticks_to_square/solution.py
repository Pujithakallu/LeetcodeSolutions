"""
Problem 473: Matchsticks to Square
=================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(matchsticks)):
                path.append(matchsticks[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
