"""
Problem 679: 24 Game
===================
Difficulty: Hard
Tags: Array, Math, Backtracking
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(cards)):
                path.append(cards[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
