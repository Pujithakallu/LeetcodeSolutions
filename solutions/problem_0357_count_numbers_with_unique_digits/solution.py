"""
Problem 357: Count Numbers with Unique Digits
============================================
Difficulty: Medium
Tags: Math, Dynamic Programming, Backtracking
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
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
