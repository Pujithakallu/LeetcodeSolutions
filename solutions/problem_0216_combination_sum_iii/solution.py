"""
Problem 216: Combination Sum III
===============================
Difficulty: Medium
Tags: Array, Backtracking
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(k)):
                path.append(k[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
