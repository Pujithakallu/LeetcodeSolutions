"""
Problem 1947: Maximum Compatibility Score Sum
===========================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(students)):
                path.append(students[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
