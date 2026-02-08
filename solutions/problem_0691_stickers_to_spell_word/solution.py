"""
Problem 691: Stickers to Spell Word
==================================
Difficulty: Hard
Tags: Array, Hash Table, String, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(stickers)):
                path.append(stickers[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
