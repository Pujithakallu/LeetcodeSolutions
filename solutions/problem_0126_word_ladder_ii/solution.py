"""
Problem 126: Word Ladder II
==========================
Difficulty: Hard
Tags: Hash Table, String, Backtracking, Breadth-First Search
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(beginWord)):
                path.append(beginWord[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
