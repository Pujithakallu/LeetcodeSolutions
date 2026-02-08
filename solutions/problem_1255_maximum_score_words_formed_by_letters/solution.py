"""
Problem 1255: Maximum Score Words Formed by Letters
=================================================
Difficulty: Hard
Tags: Array, Hash Table, String, Dynamic Programming, Backtracking, Bit Manipulation, Counting, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
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
