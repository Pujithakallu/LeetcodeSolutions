"""
Problem 401: Binary Watch
========================
Difficulty: Easy
Tags: Backtracking, Bit Manipulation
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(turnedOn)):
                path.append(turnedOn[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
