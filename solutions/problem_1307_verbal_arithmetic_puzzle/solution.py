"""
Problem 1307: Verbal Arithmetic Puzzle
====================================
Difficulty: Hard
Tags: Array, Math, String, Backtracking
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(words)):
                path.append(words[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
