"""
Problem 1774: Closest Dessert Cost
================================
Difficulty: Medium
Tags: Array, Dynamic Programming, Backtracking
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(baseCosts)):
                path.append(baseCosts[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
