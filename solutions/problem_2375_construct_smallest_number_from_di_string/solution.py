"""
Problem 2375: Construct Smallest Number From DI String
====================================================
Difficulty: Medium
Tags: String, Backtracking, Stack, Greedy
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(pattern)):
                path.append(pattern[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
