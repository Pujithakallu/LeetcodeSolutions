"""
Problem 967: Numbers With Same Consecutive Differences
=====================================================
Difficulty: Medium
Tags: Backtracking, Breadth-First Search
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
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
