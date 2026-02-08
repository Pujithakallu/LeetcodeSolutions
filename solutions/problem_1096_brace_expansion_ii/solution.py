"""
Problem 1096: Brace Expansion II
==============================
Difficulty: Hard
Tags: Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(expression)):
                path.append(expression[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
