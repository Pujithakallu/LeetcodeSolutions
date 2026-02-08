"""
Problem 1079: Letter Tile Possibilities
=====================================
Difficulty: Medium
Tags: Hash Table, String, Backtracking, Counting
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(tiles)):
                path.append(tiles[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
