"""
Problem 2178: Maximum Split of Positive Even Integers
===================================================
Difficulty: Medium
Tags: Math, Backtracking, Greedy
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(finalSum)):
                path.append(finalSum[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
