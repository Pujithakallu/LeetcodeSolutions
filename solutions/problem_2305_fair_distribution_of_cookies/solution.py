"""
Problem 2305: Fair Distribution of Cookies
========================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(cookies)):
                path.append(cookies[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
