"""
Problem 1239: Maximum Length of a Concatenated String with Unique Characters
==========================================================================
Difficulty: Medium
Tags: Array, String, Backtracking, Bit Manipulation
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def maxLength(self, arr: List[str]) -> int:
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
