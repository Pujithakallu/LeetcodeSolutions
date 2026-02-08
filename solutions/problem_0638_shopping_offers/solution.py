"""
Problem 638: Shopping Offers
===========================
Difficulty: Medium
Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(price)):
                path.append(price[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
