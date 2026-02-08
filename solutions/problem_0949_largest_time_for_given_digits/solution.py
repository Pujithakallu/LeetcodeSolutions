"""
Problem 949: Largest Time for Given Digits
=========================================
Difficulty: Medium
Tags: Array, String, Backtracking, Enumeration
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
