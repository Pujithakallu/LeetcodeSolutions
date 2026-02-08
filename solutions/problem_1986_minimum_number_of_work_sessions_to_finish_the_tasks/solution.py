"""
Problem 1986: Minimum Number of Work Sessions to Finish the Tasks
===============================================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(tasks)):
                path.append(tasks[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
