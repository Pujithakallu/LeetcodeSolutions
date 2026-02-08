"""
Problem 2048: Next Greater Numerically Balanced Number
====================================================
Difficulty: Medium
Tags: Hash Table, Math, Backtracking, Counting, Enumeration
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(n)):
                path.append(n[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
