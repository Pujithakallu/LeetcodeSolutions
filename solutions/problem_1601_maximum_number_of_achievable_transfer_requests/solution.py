"""
Problem 1601: Maximum Number of Achievable Transfer Requests
==========================================================
Difficulty: Hard
Tags: Array, Backtracking, Bit Manipulation, Enumeration
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
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
