"""
Problem 2212: Maximum Points in an Archery Competition
====================================================
Difficulty: Medium
Tags: Array, Backtracking, Bit Manipulation, Enumeration
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(numArrows)):
                path.append(numArrows[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
