"""
Problem 1276: Number of Burgers with No Waste of Ingredients
==========================================================
Difficulty: Medium
Tags: Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # Mathematical approach
        result = 0
        x = tomatoSlices
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
