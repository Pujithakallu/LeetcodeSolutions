"""
Problem 756: Pyramid Transition Matrix
=====================================
Difficulty: Medium
Tags: Hash Table, String, Backtracking, Bit Manipulation
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(bottom)):
                path.append(bottom[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
