"""
Problem 1723: Find Minimum Time to Finish All Jobs
================================================
Difficulty: Hard
Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(jobs)):
                path.append(jobs[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
